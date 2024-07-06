import json
import os

import requests
from dotenv import load_dotenv


def convert_to_rub(amount: int, _form: str) -> float:
    url = fr"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={_form}&amount={amount}"

    payload = {}
    load_dotenv()
    headers = {
        "apikey": os.getenv("Exchange_Rates_Data_API")
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    result = json.loads(response.text)['result']
    return result


print(convert_to_rub(5, "USD"))
