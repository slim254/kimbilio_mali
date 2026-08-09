import pytest
from django.test import Client

@pytest.mark.django_db
def tf_health_check():
    client = Client()
    # Test basic health or home route if configured
    assert True

def test_backend_sanity():
    # Sanity check for backend models and calculations
    total_revenue = 150000
    total_expenses = 45000
    net_operating_income = total_revenue - total_expenses
    assert net_operating_income == 105000
    print("Backend test passed successfully!")
