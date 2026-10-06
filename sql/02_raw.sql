USE SCHEMA RAW;

CREATE TABLE IF NOT EXISTS SOURCE_CATALOG (
    source_id VARCHAR,
    source_name VARCHAR,
    publisher VARCHAR,
    url VARCHAR,
    dataset VARCHAR,
    description VARCHAR,
    license VARCHAR,
    retrieval_date DATE,
    refresh_frequency VARCHAR,
    fields_used VARCHAR,
    limitations VARCHAR
);

CREATE TABLE IF NOT EXISTS ECOMMERCE_ORDERS (
    order_id VARCHAR,
    customer_id VARCHAR,
    order_date TIMESTAMP,
    status VARCHAR
);

CREATE TABLE IF NOT EXISTS PRODUCT_DATA (
    product_id VARCHAR,
    sku_id VARCHAR,
    supplier_id VARCHAR,
    category VARCHAR
);
