import masks


def mask_account_card(type_and_number: str) -> str:
    """Get card/account type and number and return string with masked number."""
    if type_and_number[:4] == "Счет":
        given_type = "Счет"
        given_number = type_and_number[5:]
        masked_number = masks.get_mask_account(given_number)
    else:
        idx = 0
        while not type_and_number[idx].isdigit():
            idx += 1
        given_type = type_and_number[:idx - 1]
        given_number = type_and_number[idx:]
        masked_number = masks.get_mask_card_number(given_number)
    return f"{given_type} {masked_number}"
