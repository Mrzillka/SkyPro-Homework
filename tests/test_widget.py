import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize("value, expected", [
    ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Счет 73654108430135874305", "Счет **4305"),
])
def test_mask_account_card(card_number, card_number_mask, account_number, account_number_mask, value, expected):
    assert mask_account_card(value) == expected
    assert mask_account_card(f"Mastercard {card_number}") == f"Mastercard {card_number_mask}"
    assert mask_account_card(f"Счет {account_number}") == f"Счет {account_number_mask}"

    with pytest.raises(TypeError):
        mask_account_card(0)


def test_get_data():
    argument_3 = '2018-07-11T02:26:18.671407'
    answer_3 = '11.07.2018'

    assert get_data(argument_3) == answer_3

    with pytest.raises(TypeError):
        get_data(0)
