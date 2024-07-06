import json

from external_api import convert_to_rub


def get_transactions_from_json(path: str) -> list[dict]:
    """Read all transactions from json file and return dict"""
    transactions_list = []
    try:
        with open(path, encoding='utf-8') as f:
            transactions_list = json.load(f)
    except Exception:
        pass
    return transactions_list


def get_transaction_amount(transaction: dict) -> float:
    """Return transaction amount in RUB"""
    amount = float(transaction['operationAmount']['amount'])
    currency_code = transaction['operationAmount']['currency']["code"]
    if currency_code == "RUB":
        return amount
    amount = convert_to_rub(amount, currency_code)
    return amount
