# Data Provenance

All downstream metrics and risk scores in SupplyShield AI are traceable back to their original source tables in the `RAW` layer.

The `CORE.V_DATA_PROVENANCE` view maintains the mapping between computed entities and original sources.

*   **OBSERVED**: Data that directly exists in the source datasets (e.g., Order placed by Customer).
*   **DERIVED**: Computed deterministically (e.g., Days of Cover, Risk Score).
*   **MAPPED**: Entity alignment across datasets (e.g., Mapping generic logistic node to a Fulfillment Center).
*   **ILLUSTRATIVE**: (If any) Scenarios injected purely for demonstrating enterprise scale without exposing confidential data.
