import re


def filter_by_state(list_of_dicts: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Return dicts with certain state value (EXECUTED by default)"""
    return list(filter(lambda dict_item: dict_item['state'] == state, list_of_dicts))


def sort_by_date(lst_of_dicts: list[dict], is_reverse: bool = True) -> list[dict]:
    """Return a new list containing all dicts in descending order sorted by 'date' value."""
    return sorted(lst_of_dicts, key=lambda d: d['date'], reverse=is_reverse)


def filter_by_description(list_of_dicts: list[dict], search: str) -> list[dict]:
    """Return a new list containing only dicts with search string in the description."""
    pattern = re.compile(rf'{search}')
    new_list = []
    for d in list_of_dicts:
        if re.search(pattern, d["description"]):
            new_list.append(d)
    return new_list
