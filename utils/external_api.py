import json
import os

import requests
from dotenv import load_dotenv


def convert_to_rub(amount: float, _form: str) -> float:
    """Convert amount of currency from any to RUB"""
    url = fr"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={_form}&amount={amount}"

    payload: dict = {}
    load_dotenv()
    headers = {
        "apikey": os.getenv("EXCHANGE_RATES_DATA_API")
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    result = float(json.loads(response.text)['result'])
    return result


def get_transaction_amount(transaction: dict) -> float:
    """Return transaction amount in RUB"""
    amount = float(transaction['operationAmount']['amount'])
    currency_code = transaction['operationAmount']['currency']["code"]
    if currency_code == "RUB":
        return amount
    amount = float(convert_to_rub(amount, currency_code))
    return amount
