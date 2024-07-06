import json
import os
from unittest.mock import patch

from dotenv import load_dotenv

from utils.external_api import convert_to_rub


@patch("requests.request")
def test_convert_to_rub(mock_request):
    mock_request.return_value = json.dumps({'result': 80.})
    assert convert_to_rub(1, "USD") == 80.
    url = fr"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1"
    load_dotenv()
    headers = {
        "apikey": os.getenv("Exchange_Rates_Data_API")
    }
    mock_request.assert_called_ones_with("GET", url, headers=headers, data={})
