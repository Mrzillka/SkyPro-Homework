import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_number, card_number_mask):
    argument_1 = '7000792289606361'
    answer_1 = '7000 79** **** 6361'
    assert get_mask_card_number(argument_1) == answer_1
    assert get_mask_card_number(card_number) == card_number_mask

    with pytest.raises(AttributeError):
        get_mask_card_number(0)


def test_get_mask_account(account_number, account_number_mask):
    argument_2 = '73654108430135874305'
    answer_2 = '**4305'
    assert get_mask_account(argument_2) == answer_2
    assert get_mask_account(account_number) == account_number_mask

    with pytest.raises(AttributeError):
        get_mask_account(0)
