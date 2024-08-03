import pytest

from src.processing import *


def test_filter_by_state(users_data):
    answer_executed = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]
    answer_canceled = [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]

    assert filter_by_state(users_data, 'EXECUTED') == answer_executed
    assert filter_by_state(users_data, 'CANCELED') == answer_canceled

    with pytest.raises(KeyError):
        filter_by_state([{}], "")


def test_sort_by_date(users_data):
    answer_sorted = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]

    assert sort_by_date(users_data) == answer_sorted


def test_filter_by_description(users_data_with_description):
    answer_filtered = [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'description': '23'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689', 'description': '34'},
    ]
    assert filter_by_description(users_data_with_description, "3") == answer_filtered


def test_count_transactions_by_type():
    transactions = [
        {"description": "Перевод со счета"},
        {"description": "Перевод на счет"},
        {"description": "Открытие вклада"},
        {"description": "Закрытие перевода"},
    ]
    answer = {
        'Перевод': 3,
        'Перевод на счет': 1,
        'Открытие': 1
    }
    assert count_transactions_by_type(transactions, ["Перевод", "Перевод на счет", "Открытие"]) == answer

