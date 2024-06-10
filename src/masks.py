def get_mask_card_number(card_number: int | str) -> str:
    """Return a mask of 16-simbols card number in following format XXXX XX** **** XXXX."""
    try:
        card_number = str(card_number)
    finally:
        card_number = card_number.replace(" ", "")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: int | str) -> str:
    """Return a mask of 20-simbols number in following format **XXXX."""
    try:
        account_number = str(account_number)
    finally:
        account_number = account_number.replace(" ", "")
    return f"**{account_number[-4:]}"
