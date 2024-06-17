def filter_by_state(lst_of_dicts: list[dict], state: str) -> list[dict]:
    new_lst = []
    for d in lst_of_dicts:
        if d['state'] == state:
            new_lst.append(d)
    return new_lst


def sort_by_date(lst_of_dicts: list[dict], reverse: bool = False) -> list[dict]:
    return sorted(lst_of_dicts, key=lambda d: d['date'], reverse=not reverse)
