import json
import logging
from typing import Any

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                    filename=r'logs/utils_logs.log',
                    filemode='w')

logger = logging.getLogger(__name__)

logger.info(f"Using module utils")


def get_transactions_from_json(path: str) -> Any:
    """Read all transactions from json file and return dict"""
    logger.debug("Function 'get_mask_card_number' was called")
    try:
        logger.info(f"Try to open json file {path}")
        with open(path, encoding='utf-8') as f:
            logger.info("Try to load json file")
            transactions_list = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.warning("File not found or can't be converted from json")
        return []
    return transactions_list
