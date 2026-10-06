import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="SupplyShield AI", layout="wide")

st.markdown("""
    <style>
    .big-font { font-size:30px !important; font-weight: bold; }
    .kpi-val { font-size: 24px; font-weight: bold; color: #ff4b4b; }
    .kpi-title { font-size: 14px; color: #666; }
    .card { background-color: #1e1e1e; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

st.title("SupplyShield AI")
st.subheader("E-Commerce Supply Chain Control Tower")
st.markdown("*From supplier disruption to customer impact.*")

st.markdown("---")

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Revenue at Risk", "₹ 450,000", "-15%", delta_color="inverse")
col2.metric("SKUs at Risk", "24", "+3", delta_color="inverse")
col3.metric("FCs Exposed", "3", "0", delta_color="off")
col4.metric("Delayed Inbound", "12", "+2", delta_color="inverse")
col5.metric("Suppliers at Risk", "4", "-1", delta_color="inverse")

st.markdown("---")

st.header("Conversational Analytics")
question = st.selectbox("ASK SUPPLYSHIELD", [
    "Which supplier disruptions could cause customer-facing fulfillment failures, and what should we act on first?",
    "Which suppliers are putting our Hyderabad fulfillment center at risk, and which customer orders are affected?",
    "Which SKUs have the highest stockout risk?"
])

if st.button("Analyze Risk"):
    st.markdown("### Answer")
    st.info("**Nova Components** is currently experiencing a 4-day inbound delay affecting **SKU-204**, pushing days of cover at **Hyderabad FC** below the 5-day critical threshold.")
    
    st.markdown("### Why It Matters")
    st.write("This delay exposes safety stock, directly threatening SLA compliance for pending customer orders.")
    
    st.markdown("### Supply-Chain Chain")
    st.code("Nova Components -> SKU-204 -> Hyderabad FC -> Inbound Delay (4 days) -> 150 Orders Exposed")
    
    st.markdown("### Customer Impact")
    st.error("₹ 450,000 Revenue at Risk | 120 Unique Customers Affected")
    
    st.markdown("### Recommended Action")
    st.success("Expedite inbound shipment PO-8892 and redistribute 50 units from Bangalore FC.")
    
    st.markdown("### Data Trust & Provenance")
    st.caption("Derived from OBSERVED ERP Data | Metrics: DAYS_OF_COVER, REVENUE_AT_RISK | Quality: HEALTHY")

st.markdown("---")
st.header("Risk Radar & Downstream Impact")
data = pd.DataFrame({
    'Supplier': ['Nova Components', 'Global Logistics', 'TechMakers'],
    'SKU': ['SKU-204', 'SKU-891', 'SKU-102'],
    'FC': ['Hyderabad FC', 'Mumbai FC', 'Delhi FC'],
    'Risk Level': ['CRITICAL', 'HIGH', 'MEDIUM'],
    'Rev at Risk (₹)': [450000, 120000, 45000],
    'Orders Exposed': [150, 45, 12]
})
st.dataframe(data, use_container_width=True)
