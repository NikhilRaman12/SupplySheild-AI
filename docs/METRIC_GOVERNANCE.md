# Governed Metric Catalog

## 1. DAYS_OF_COVER
*   **business_definition**: The number of days the current inventory will last based on average daily demand.
*   **formula**: `Available Inventory / Average Daily Demand`
*   **grain**: SKU per Fulfillment Center
*   **source**: `ANALYTICS.V_SKU_STOCKOUT_RISK`
*   **synonyms**: `inventory runway`, `days on hand`
*   **example_questions**: "What is the days of cover for SKU-204 at Hyderabad FC?"

## 2. REVENUE_AT_RISK
*   **business_definition**: Total unfulfilled order value that is exposed due to inventory stockouts or delayed inbound shipments.
*   **formula**: `SUM(Order Value) where Order Status = 'OPEN' and SKU Risk Level in ('HIGH', 'CRITICAL')`
*   **grain**: Aggregate (Customer, FC, SKU, Supplier)
*   **source**: `ANALYTICS.V_DOWNSTREAM_IMPACT`
*   **synonyms**: `exposed revenue`, `sales at risk`
*   **example_questions**: "How much revenue is currently at risk due to supplier delays?"

## 3. SUPPLIER_RISK_SCORE
*   **business_definition**: A composite score indicating the likelihood of a supplier causing supply chain disruptions.
*   **formula**: `(Delayed Shipments / Total Shipments) * Delay Severity Factor + Quality Defect Rate`
*   **grain**: Supplier
*   **source**: `ANALYTICS.V_SUPPLIER_PERFORMANCE`
*   **synonyms**: `supplier reliability`, `vendor risk`
*   **example_questions**: "Which suppliers have the worst on-time performance?"
