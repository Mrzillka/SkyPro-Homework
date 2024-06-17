def filter_by_state(list_of_dicts: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Return dicts with certain state value (EXECUTED by default)"""
    return list(filter(lambda dict_item: True if dict_item['state'] == state else False, list_of_dicts))


def sort_by_date(lst_of_dicts: list[dict], is_reverse: bool = True) -> list[dict]:
    """Return a new list containing all dicts in descending order sorted by 'date' value."""
    return sorted(lst_of_dicts, key=lambda d: d['date'], reverse=is_reverse)
