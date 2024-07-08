from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Get card/account type and number and return string with masked number."""
    if type_and_number[:4] == "Счет":
        given_type = "Счет"
        given_number = type_and_number[5:]
        masked_number = get_mask_account(given_number)
    else:
        idx = 0
        while not type_and_number[idx].isdigit():
            idx += 1
        given_type = type_and_number[: idx - 1]
        given_number = type_and_number[idx:]
        masked_number = get_mask_card_number(given_number)
    return f"{given_type} {masked_number}"


def get_data(full_time: str) -> str:
    """Return date in “dd.mm.yyyy” format"""
    year = full_time[:4]
    month = full_time[5:7]
    day = full_time[8:10]
    return ".".join((day, month, year))
