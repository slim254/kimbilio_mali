def test_sample_profitability_calculation():
    rental_income = 12000
    maintenance_cost = 2500
    property_tax = 1500
    net_profit = rental_income - (maintenance_cost + property_tax)
    assert net_profit == 8000
    print("Root backend test passed!")
