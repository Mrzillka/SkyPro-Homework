import json


def get_transactions_from_json(path: str) -> list[dict]:
    """Read all transactions from json file and return dict"""
    try:
        with open(path, encoding='utf-8') as f:
            transactions_list = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    return transactions_list
