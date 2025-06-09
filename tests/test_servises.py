from src.services import *


def test_investment_bank(transactions):
    month = "2019-03"
    limit = 10
    assert round(investment_bank(month, transactions, limit), 2) == 1.66
