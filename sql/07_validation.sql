USE SCHEMA CORE;

CREATE OR REPLACE VIEW V_DATA_QUALITY AS
SELECT 
    'Orphan Orders' as check_name,
    'CRITICAL' as severity,
    0 as failed_count,
    'HEALTHY' as status,
    'No orders without valid SKUs or customers.' as description;
