# Data Quality

SupplyShield maintains rigorous data quality checks in `CORE.V_DATA_QUALITY`.

Checks include:
*   **Orphan Orders**: Orders with no corresponding customer or SKU.
*   **Missing Locations**: Fulfillment Centers or Suppliers with unresolvable geographic coordinates.
*   **Negative Quantities**: Inventory or order quantities < 0.
*   **Freshness**: Stale data exceeding acceptable latency thresholds.

Status Levels:
*   `HEALTHY`: Metric within acceptable bounds.
*   `WARNING`: Minor anomalies detected, investigate.
*   `CRITICAL`: Severe data integrity issues, metrics may be compromised.
