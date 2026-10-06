import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="SupplyShield AI", layout="wide")

st.markdown("""
    <style>
    .big-font { font-size:30px !important; font-weight: bold; }
    .kpi-val { font-size: 24px; font-weight: bold; color: #ff4b4b; }
    .kpi-title { font-size: 14px; color: #666; }
    .card { background-color: #1e1e1e; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    base_path = os.path.join("docs", "data_cortex")
    orders = pd.read_csv(os.path.join(base_path, "orders.csv"))
    shipments = pd.read_csv(os.path.join(base_path, "shipments.csv"))
    products = pd.read_csv(os.path.join(base_path, "products.csv"))
    order_items = pd.read_csv(os.path.join(base_path, "order_items.csv"))
    
    # Merge data
    df = shipments.merge(orders, on='order_id').merge(order_items, on='order_id').merge(products, on='product_id')
    return df

df = load_data()
delayed = df[df['delayed_flag'] == 1]

# De-duplicate orders to get correct final amount sum, or just use item_revenue. We'll use item_revenue to be safe with items.
rev_at_risk = delayed['item_revenue'].sum()
skus_at_risk = delayed['product_id'].nunique()
fcs_exposed = delayed['warehouse_city'].nunique()
delayed_shipments = delayed['shipment_id'].nunique()
suppliers_at_risk = delayed['brand'].nunique()

st.title("SupplyShield AI")
st.subheader("E-Commerce Supply Chain Control Tower")
st.markdown("*From supplier disruption to customer impact.*")

st.markdown("---")

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Revenue at Risk", f"₹ {rev_at_risk:,.0f}")
col2.metric("SKUs at Risk", skus_at_risk)
col3.metric("FCs Exposed", fcs_exposed)
col4.metric("Delayed Shipments", delayed_shipments)
col5.metric("Suppliers at Risk", suppliers_at_risk)

st.markdown("---")

st.header("Risk Radar & Downstream Impact")

risk_data = delayed.groupby(['brand', 'product_name', 'warehouse_city']).agg(
    orders_exposed=('order_id', 'nunique'),
    rev_at_risk=('item_revenue', 'sum')
).reset_index()

risk_data.rename(columns={
    'brand': 'Supplier',
    'product_name': 'Product',
    'warehouse_city': 'FC',
    'orders_exposed': 'Orders Exposed',
    'rev_at_risk': 'Rev at Risk (₹)'
}, inplace=True)

# Add Risk Level based on revenue at risk
def get_risk_level(rev):
    if rev > 500000:
        return 'CRITICAL'
    elif rev > 100000:
        return 'HIGH'
    else:
        return 'MEDIUM'

risk_data['Risk Level'] = risk_data['Rev at Risk (₹)'].apply(get_risk_level)
risk_data = risk_data.sort_values('Rev at Risk (₹)', ascending=False).head(50)

st.dataframe(risk_data[['Supplier', 'Product', 'FC', 'Risk Level', 'Rev at Risk (₹)', 'Orders Exposed']], use_container_width=True)

st.markdown("---")
st.header("Conversational Analytics")

if not risk_data.empty:
    top_risk = risk_data.iloc[0]
    question = st.selectbox("ASK SUPPLYSHIELD", [
        f"Which supplier disruptions could cause customer-facing fulfillment failures at {top_risk['FC']}?",
        "Which SKUs have the highest stockout risk?",
        "Show me all critical risk levels."
    ])
    
    if st.button("Analyze Risk"):
        st.markdown("### Answer")
        st.info(f"**{top_risk['Supplier']}** is currently experiencing delays affecting **{top_risk['Product']}** at **{top_risk['FC']}**.")
        
        st.markdown("### Why It Matters")
        st.write("This delay directly threatens SLA compliance for pending customer orders and could lead to significant revenue loss.")
        
        st.markdown("### Supply-Chain Chain")
        st.code(f"{top_risk['Supplier']} -> {top_risk['Product']} -> {top_risk['FC']} -> Delayed Shipments -> {top_risk['Orders Exposed']} Orders Exposed")
        
        st.markdown("### Customer Impact")
        st.error(f"₹ {top_risk['Rev at Risk (₹)']:,.0f} Revenue at Risk | {top_risk['Orders Exposed']} Orders Affected")
        
        st.markdown("### Recommended Action")
        st.success(f"Expedite inbound shipments for {top_risk['Product']} and explore alternate fulfillment options at {top_risk['FC']}.")
        
        st.markdown("### Data Trust & Provenance")
        st.caption("Derived from OBSERVED ERP Data | Metrics: DELAYED_FLAG, ITEM_REVENUE | Quality: HEALTHY")
