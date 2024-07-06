import json
import os
from unittest.mock import patch

from dotenv import load_dotenv

from utils.external_api import convert_to_rub, get_transaction_amount


@patch("requests.request")
def test_convert_to_rub(mock_request):
    mock_request.return_value.text = json.dumps({'result': 80.})
    assert convert_to_rub(1, "USD") == 80.
    url = fr"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1"
    load_dotenv()
    headers = {
        "apikey": os.getenv("Exchange_Rates_Data_API")
    }
    mock_request.assert_called_once_with("GET", url, headers=headers, data={})


@patch("utils.external_api.convert_to_rub")
def test_get_transaction_amount(mock_convert, single_transaction):
    mock_convert.return_value = 80
    assert get_transaction_amount(single_transaction) == 80.0
    mock_convert.assert_called_once_with(1, "USD")
