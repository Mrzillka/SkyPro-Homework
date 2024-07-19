import _io
import csv
import json
import logging
import pandas as pd
from typing import Any

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                    filename=r'logs/utils_logs.log',
                    # filename=r'utils_logs.log',
                    filemode='w')

logger = logging.getLogger(__name__)

logger.info(f"Using module utils")


def get_transactions(path: str) -> Any:
    """Read all transactions from file and return dict"""
    logger.debug("Function 'get_transactions' was called")
    file_format = path[path.rfind('.'):]
    try:
        logger.info(f"Try to open file {path}")
        if file_format == ".xlsx":
            transactions_list = get_transactions_from_excel(path)
        else:
            with open(path, encoding="utf-8") as f:
                logger.info("File was opened")
                if file_format == ".json":
                    transactions_list = get_transactions_from_json(f)
                elif file_format == ".csv":
                    transactions_list = get_transactions_from_csv(f)
                else:
                    logger.warning(f"Unsupported file format {file_format}")
                    transactions_list = []
    except FileNotFoundError:
        logger.warning(f"File {path} not found")
        return []
    return transactions_list


def get_transactions_from_json(json_obj: _io.TextIOWrapper) -> Any:
    """Load transactions from json file"""
    try:
        logger.info("Try to load json file")
        transactions_list = json.load(json_obj)
    except json.JSONDecodeError:
        logger.warning("File can't be converted from json")
        return []
    return transactions_list


def get_transactions_from_csv(csv_obj: _io.TextIOWrapper) -> Any:
    """Load transactions from csv file"""
    reader = csv.DictReader(csv_obj, delimiter=";")
    transactions_list = []
    for row in reader:
        transactions_list.append(row)
    return transactions_list


def get_transactions_from_excel(path) -> Any:
    """Load transactions from exel file"""
    excel_obj = pd.read_excel(path)
    return excel_obj.to_dict(orient="records")


get_transactions_from_excel("transactions_excel.xlsx")
