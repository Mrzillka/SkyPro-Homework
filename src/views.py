import os
from datetime import datetime
import json
from typing import Any, Dict, List

import requests
from dotenv import load_dotenv

from external_api import convert_to_rub
from src.utils import get_transactions_from_csv


def main_page() -> json.JSONDecoder:
    settings = json.loads(open(os.path.abspath(os.path.join(os.pardir, "data/user-settings.json")), mode='r').read())
    transactions = get_transactions_from_csv(
        open(os.path.abspath(os.path.join(os.pardir, "data/operations.csv")),
             encoding='UTF-8'),
        delimiter=',')

    d = {
        'greeting': greetings(),
        'cards': get_cards_spending_and_cashback(transactions),
        'top_transactions': get_top5_transactions(transactions),
        'currency_rates': get_currencies_exchange_rate(settings['user_currencies']),
        'stock_prices': get_stocks_exchange_rate(settings['user_stocks'])
    }
    for key in d:
        print(f"'{key}': {d[key]}")


def greetings() -> str:
    """Return appropriate greeting for current user time"""
    now = datetime.now().time()
    hour, minute = now.hour, now.minute
    if hour < 6 or hour == 6 and minute == 0:
        return "Доброй ночи"
    if hour < 12 or hour == 12 and minute == 0:
        return "Доброе утро"
    if hour < 18 or hour == 18 and minute == 0:
        return "Добрый день"
    return "Добрый вечер"


def get_operations_for_month(transactions: List[dict[Any, Any]], month: str = None):
    """Returns list of all transactions from beginning of current or given month"""
    month_transactions = []
    if not month:
        month = datetime.now().date()
    else:
        month = datetime.strptime(month, "%d.%m.%Y").date()
    to_ = month
    from_ = month.replace(day=1)
    transactions.sort(
        reverse=True,
        key=lambda date: datetime.strptime(date["Дата операции"], "%d.%m.%Y %H:%M:%S")
    )
    for transaction in transactions:
        date = datetime.strptime(transaction["Дата операции"], "%d.%m.%Y %H:%M:%S").date()
        if date > to_:
            continue
        if date < from_:
            break
        month_transactions.append(transaction)
    return month_transactions


def get_cards_spending_and_cashback(transactions: List[dict[str, Any]]) -> List[Dict[str, str | float]]:
    """Returns sum of all negative transactions and cashback for every card in given transaction list"""
    cards_spending = {}
    for transaction in transactions:
        amount = float(transaction['Сумма операции'].replace(',', '.'))
        if amount > 0:
            continue
        if transaction['Номер карты'] not in cards_spending.keys():
            cards_spending[transaction['Номер карты']] = {
                'total_spent': amount,
                'cashback': int(transaction['Кэшбэк']) if transaction['Кэшбэк'] else 0,
            }
        else:
            cards_spending[transaction['Номер карты']]['total_spent'] += amount
            cards_spending[transaction['Номер карты']]['cashback'] -= amount / 100
    for card in cards_spending:
        cards_spending[card]['total_spent'] = round(cards_spending[card]['total_spent'], 2)
        cards_spending[card]['cashback'] = round(cards_spending[card]['cashback'], 2)

    cards_spending = [
        {
            'last_digits': card[1:],
            'total_spent': cards_spending[card]['total_spent'],
            'cashback': cards_spending[card]['cashback']
        }
        for card in cards_spending
    ]
    return cards_spending


def get_top5_transactions(transactions: List[Dict[str, Any]]) -> list[dict[str, Any]]:
    transactions.sort(reverse=True, key=lambda tr: abs(float(tr['Сумма операции'].replace(',', '.'))))
    top_transactions = [
        {
            'date': tr['Дата платежа'],
            'amount': tr['Сумма операции'],
            'category': tr['Категория'],
            'description': tr['Описание'],
        }
        for tr in transactions[:5]
    ]
    return top_transactions


def get_currencies_exchange_rate(currencies: list[str]) -> list[dict[str, str | float]]:
    currency_rates = [{'currency': cur} for cur in currencies]

    for d in currency_rates:
        from_ = d['currency']
        res = convert_to_rub(1, from_)
        d['rate'] = res

    return currency_rates


def get_stocks_exchange_rate(stocks: list[str]) -> list[dict[str, str | float]]:
    load_dotenv()
    function = 'GLOBAL_QUOTE'
    apikey = os.getenv("ALPHAVINTAGE_API"),

    stock_rates = [{'stock': stk} for stk in stocks]

    for d in stock_rates:
        symbol = d['stock']
        url = fr"https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={apikey}"
        response = requests.get(url)
        data = response.json()
        func = " ".join(function.replace("_", " ").title().split())
        price = float(data[func]['05. price'])
        d['price'] = price

    return stock_rates


main_page()
