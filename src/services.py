from typing import List, Dict, Any

from src.external_api import convert_to_rub


def investment_bank(month: str, transactions: List[Dict[str, Any]], limit: int) -> float:
    """Calculates the amount of investments to bank for given month with given round limit"""
    investments = .0
    for transaction in transactions:
        if month in transaction['date']:
            amount = float(transaction['operationAmount']['amount'])
            currency = transaction['operationAmount']['currency']['code']
            if currency != "RUB":
                amount = convert_to_rub(amount, currency)
            investments += -amount % limit
    return round(investments, 2)
