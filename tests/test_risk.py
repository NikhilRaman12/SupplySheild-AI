from supplyshield.risk.features import calculate_supplier_score

def test_calculate_supplier_score():
    assert calculate_supplier_score(10, 5) == 8.5
