# Snowpark Python Architecture

Snowpark is used where it provides genuine engineering value over standard SQL:

1.  **Normalization (`src/supplyshield/normalization/`)**: Complex string matching, regex parsing, and categorization of messy product text.
2.  **Entity Resolution (`src/supplyshield/ontology/`)**: Mapping disparate supplier names or customer records using fuzzy matching algorithms.
3.  **Risk Feature Engineering (`src/supplyshield/risk/`)**: Developing complex statistical features for risk scoring that are cumbersome in SQL.
4.  **Validation (`src/supplyshield/quality/`)**: Complex procedural data quality rules.
