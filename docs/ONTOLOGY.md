# E-Commerce Supply Chain Ontology

## Primary Entities

### Supplier
*   **business_definition**: An external organization providing raw materials or finished products.
*   **primary_key**: `supplier_id`
*   **important_attributes**: `supplier_name`, `country`, `reliability_score`, `lead_time_days`
*   **source**: `RAW.PRODUCT_DATA`
*   **relationships**: `Supplier -> SKU` (1:N), `Supplier -> Purchase Order` (1:N)
*   **cardinality**: One supplier to many SKUs
*   **governance_notes**: Must resolve to a single canonical entity.
*   **provenance**: Sourced from supplier catalog.

### SKU (Stock Keeping Unit)
*   **business_definition**: A unique identifier for each distinct product and variant.
*   **primary_key**: `sku_id`
*   **important_attributes**: `product_id`, `category`, `unit_cost`, `retail_price`
*   **source**: `RAW.PRODUCT_DATA`
*   **relationships**: `SKU -> Inventory` (1:N), `SKU -> Shipment` (1:N), `Customer Order -> SKU` (N:1)
*   **cardinality**: One SKU mapped to many inventory locations.
*   **governance_notes**: Universal key across all domains.
*   **provenance**: Master Data Management (MDM).

### Fulfillment Center
*   **business_definition**: A physical facility where inventory is stored and orders are fulfilled.
*   **primary_key**: `fc_id`
*   **important_attributes**: `fc_name`, `location_id`, `capacity`, `current_utilization`
*   **source**: `RAW.LOGISTICS_DATA`
*   **relationships**: `Fulfillment Center -> Inventory` (1:N)
*   **cardinality**: One FC stores many SKUs.
*   **governance_notes**: Location IDs must match standardized location tables.
*   **provenance**: Logistics dataset.

### Inventory
*   **business_definition**: Stock levels of a specific SKU at a specific fulfillment center.
*   **primary_key**: `inventory_id` (or composite `sku_id` + `fc_id`)
*   **important_attributes**: `quantity_on_hand`, `allocated_quantity`, `available_quantity`
*   **source**: `RAW.LOGISTICS_DATA`
*   **relationships**: `Inventory -> SKU` (N:1), `Inventory -> Fulfillment Center` (N:1)
*   **cardinality**: Many-to-One.
*   **governance_notes**: Calculated daily.
*   **provenance**: ERP snapshot.

### Shipment (Inbound)
*   **business_definition**: Movement of goods from supplier to fulfillment center.
*   **primary_key**: `shipment_id`
*   **important_attributes**: `po_id`, `origin`, `destination`, `expected_arrival_date`, `status`, `delay_days`
*   **source**: `RAW.FREIGHT_DATA`
*   **relationships**: `Supplier -> Shipment` (1:N), `Shipment -> Fulfillment Center` (N:1)
*   **cardinality**: Many shipments per supplier.
*   **governance_notes**: Tracked via carrier milestones.
*   **provenance**: Transportation Management System.

### Customer Order
*   **business_definition**: A confirmed request from a customer to purchase items.
*   **primary_key**: `order_id`
*   **important_attributes**: `customer_id`, `order_date`, `status`, `total_value`
*   **source**: `RAW.ECOMMERCE_ORDERS`
*   **relationships**: `Customer Order -> SKU` (1:N), `Customer Order -> Customer` (N:1)
*   **cardinality**: Many orders per customer.
*   **governance_notes**: Financial source of truth.
*   **provenance**: E-commerce platform.

### Customer
*   **business_definition**: An individual or entity that purchases goods.
*   **primary_key**: `customer_id`
*   **important_attributes**: `customer_name`, `segment`, `location_id`
*   **source**: `RAW.CUSTOMER_DATA`
*   **relationships**: `Customer -> Customer Order` (1:N)
*   **cardinality**: One customer, many orders.
*   **governance_notes**: PII protected.
*   **provenance**: CRM.

## Core Relationships

*   **Supplier -> Product / SKU**: `source_entity`: Supplier, `target_entity`: SKU. `business_meaning`: Manufactures or provides the SKU. `source`: OBSERVED.
*   **Product / SKU -> Fulfillment Center**: `source_entity`: SKU, `target_entity`: Fulfillment Center. `business_meaning`: Stored at location. `source`: OBSERVED.
*   **Fulfillment Center -> Inventory**: `source_entity`: Fulfillment Center, `target_entity`: Inventory. `business_meaning`: Holds specific quantity. `source`: OBSERVED.
*   **Inventory -> Inbound Shipment**: `source_entity`: Inventory, `target_entity`: Shipment. `business_meaning`: Replenishment source. `source`: DERIVED.
*   **Inbound Shipment -> Customer Order**: `source_entity`: Shipment, `target_entity`: Customer Order. `business_meaning`: Fulfills dependent orders (risk link). `source`: DERIVED.
*   **Customer Order -> Customer**: `source_entity`: Customer Order, `target_entity`: Customer. `business_meaning`: Placed by. `source`: OBSERVED.
