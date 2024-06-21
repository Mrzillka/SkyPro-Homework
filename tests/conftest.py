import pytest


@pytest.fixture
def card_number():
    return "1234 5678 9100 0000"


@pytest.fixture
def card_number_mask():
    return "1234 56** **** 0000"


@pytest.fixture
def account_number():
    return '01234567890123456789'


@pytest.fixture
def account_number_mask():
    return "**6789"


@pytest.fixture
def users_data():
    lst = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]
    return lst
