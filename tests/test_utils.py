import json
import os
from unittest.mock import patch

from utils.utils import get_transactions_from_json


def test_get_transactions_from_json(transactions):
    with open("tr.json", "w") as f:
        json.dump(transactions, f)
    assert get_transactions_from_json("tr.json") == transactions
    os.remove("tr.json")
