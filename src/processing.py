import collections
import re


def filter_by_state(list_of_transactions: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Return dicts with certain state value (EXECUTED by default)"""
    return list(filter(lambda dict_item: dict_item and dict_item['state'] == state, list_of_transactions))


def sort_by_date(list_of_transactions: list[dict], is_reverse: bool = True) -> list[dict]:
    """Return a new list containing all dicts in descending order sorted by 'date' value."""
    return sorted(list_of_transactions, key=lambda d: d['date'], reverse=is_reverse)


def filter_by_description(list_of_transactions: list[dict], search: str) -> list[dict]:
    """Return a new list containing only dicts with search string in the description."""
    pattern = re.compile(rf'{search}')
    new_list = []
    for transaction in list_of_transactions:
        if re.search(pattern, transaction["description"]):
            new_list.append(transaction)
    return new_list


def count_transactions_by_type(list_of_transactions: list[dict], categories: list[str]) -> dict:
    """Return a dict, containing count of operations by categories"""
    counter: collections.defaultdict = collections.defaultdict(int)
    for transaction in list_of_transactions:
        for category in categories:
            if re.search(rf"{category}", transaction["description"], re.IGNORECASE):
                counter[category] += 1
    return dict(counter)
