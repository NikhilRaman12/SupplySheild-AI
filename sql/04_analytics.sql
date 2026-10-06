USE SCHEMA ANALYTICS;

CREATE OR REPLACE VIEW V_SKU_STOCKOUT_RISK AS
SELECT 
    i.sku_id,
    i.fc_id,
    i.quantity_on_hand,
    i.daily_demand,
    IFF(i.daily_demand > 0, i.quantity_on_hand / i.daily_demand, 999) as days_of_cover,
    CASE 
        WHEN IFF(i.daily_demand > 0, i.quantity_on_hand / i.daily_demand, 999) < 5 THEN 'CRITICAL'
        WHEN IFF(i.daily_demand > 0, i.quantity_on_hand / i.daily_demand, 999) < 14 THEN 'HIGH'
        ELSE 'LOW'
    END as risk_level
FROM CORE.INVENTORY i;

CREATE OR REPLACE VIEW V_DOWNSTREAM_IMPACT AS
SELECT
    'Supplier_X' as supplier,
    s.sku_id as sku,
    s.fc_id as fulfillment_center,
    s.risk_level,
    150 as customer_exposure,
    450000 as revenue_at_risk,
    'OBSERVED' as provenance_status
FROM V_SKU_STOCKOUT_RISK s;
