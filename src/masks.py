import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                    filename=r'logs/masks_logs.log',
                    filemode='w')

logger = logging.getLogger(__name__)

logger.info("Using module masks")


def get_mask_card_number(card_number: str) -> str:
    """Return a mask of 16-simbols card number in following format XXXX XX** **** XXXX."""
    logger.info("Function 'get_mask_card_number' was called")
    card_number = card_number.replace(" ", "")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Return a mask of 20-simbols number in following format **XXXX."""
    logger.info("Function 'get_mask_account' was called")
    account_number = account_number.replace(" ", "")
    return f"**{account_number[-4:]}"
