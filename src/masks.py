def get_mask_card_number(card_number: str) -> str:
    """Return a mask of 16-simbols card number in following format XXXX XX** **** XXXX."""
    card_number = str(card_number)
    card_number = card_number.replace(" ", "")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Return a mask of 20-simbols number in following format **XXXX."""
    account_number = str(account_number)
    account_number = account_number.replace(" ", "")
    return f"**{account_number[-4:]}"
