import os.path
from datetime import datetime
from functools import wraps
from typing import Any, Optional

import pandas as pd
from dateutil.relativedelta import relativedelta


def report(func) -> Any | None:
    """Write report data into file"""

    @wraps(func)
    def inner(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)

        with open(os.path.join(os.path.curdir, "logs", f"{func.__name__} {datetime.now().date()}.txt"),
                  mode='w',
                  encoding='UTF-8') as file:
            with pd.option_context('display.max_rows', 20000, 'display.max_columns', 1000):
                file.write(result.to_string(line_width=None))

        return result

    return inner


@report
def spending_by_category(transactions: pd.DataFrame,
                         category: str,
                         date: Optional[str] = None) -> pd.DataFrame:
    """Returns all transactions in given category for last three month from given date"""
    if not date:
        date = pd.Timestamp.now()
    date = pd.to_datetime(date, format='%d-%M-%Y')
    transactions['Дата операции'] = pd.to_datetime(transactions['Дата операции'], dayfirst=True)

    now = date
    three_month_ago = now - relativedelta(months=3)

    three_month_transactions = transactions.loc[
        (transactions['Дата операции'] <= now) &
        (transactions['Дата операции'] >= three_month_ago) &
        (transactions['Категория'] == category)
        ]
    return three_month_transactions
