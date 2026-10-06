def calculate_supplier_score(delay_days, defect_rate):
    return (delay_days * 0.7) + (defect_rate * 0.3)
