USE SCHEMA CORE;

CREATE TABLE IF NOT EXISTS SUPPLIERS (
    supplier_id VARCHAR PRIMARY KEY,
    supplier_name VARCHAR,
    country VARCHAR
);

CREATE TABLE IF NOT EXISTS SKUS (
    sku_id VARCHAR PRIMARY KEY,
    product_id VARCHAR,
    category VARCHAR
);

CREATE TABLE IF NOT EXISTS FULFILLMENT_CENTERS (
    fc_id VARCHAR PRIMARY KEY,
    fc_name VARCHAR,
    location_id VARCHAR
);

CREATE TABLE IF NOT EXISTS INVENTORY (
    inventory_id VARCHAR PRIMARY KEY,
    sku_id VARCHAR,
    fc_id VARCHAR,
    quantity_on_hand INT,
    daily_demand FLOAT
);

CREATE TABLE IF NOT EXISTS DATA_PROVENANCE (
    source_id VARCHAR,
    source_name VARCHAR,
    publisher VARCHAR,
    dataset_name VARCHAR,
    source_url VARCHAR,
    license VARCHAR,
    license_url VARCHAR,
    dataset_version VARCHAR,
    retrieval_timestamp TIMESTAMP,
    transformation VARCHAR,
    provenance_status VARCHAR,
    row_count INT
);
