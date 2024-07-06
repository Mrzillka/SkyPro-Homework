import json
import os
from unittest.mock import patch

from utils.utils import get_transactions_from_json, get_transaction_amount


def test_get_transactions_from_json(transactions):
    with open("tr.json", "w") as f:
        json.dump(transactions, f)
    assert get_transactions_from_json("tr.json") == transactions
    os.remove("tr.json")


@patch("utils.utils.convert_to_rub")
def test_get_transaction_amount(mock_convert, single_transaction):
    mock_convert.return_value = 80
    assert get_transaction_amount(single_transaction) == 80.0
    mock_convert.assert_called_once_with(1, "USD")
