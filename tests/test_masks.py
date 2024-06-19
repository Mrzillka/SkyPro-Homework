import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("value, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1596837868705199", "1596 83** **** 5199"),
    ("7158300734726758", "7158 30** **** 6758"),
    ("6831982476737658", "6831 98** **** 7658"),
    ("8990 9221 1366 5229", "8990 92** **** 5229"),
    ("5999 4142 2842 6353", "5999 41** **** 6353"),
])
def test_get_mask_card_number(card_number, card_number_mask, value, expected):
    assert get_mask_card_number(value) == expected
    assert get_mask_card_number(card_number) == card_number_mask

    with pytest.raises(AttributeError):
        get_mask_card_number(0)


@pytest.mark.parametrize("value, expected", [
    ("73654108430135874305", "**4305"),
    ("64686473678894779589", "**9589"),
    ("35383033474447895560", "**5560"),
    ("73654108430135874305", "**4305"),
])
def test_get_mask_account(account_number, account_number_mask, value, expected):
    assert get_mask_account(value) == expected
    assert get_mask_account(account_number) == account_number_mask

    with pytest.raises(AttributeError):
        get_mask_account(0)
