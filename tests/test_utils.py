import json
import os

from utils.utils import get_transactions


def test_get_transactions_from_json(transactions):
    with open("tr.json", "w") as f:
        json.dump(transactions, f)
    assert get_transactions("tr.json") == transactions
    os.remove("tr.json")
