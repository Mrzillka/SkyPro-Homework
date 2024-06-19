import pytest

from src.widget import mask_account_card, get_data


def test_mask_account_card(card_number, card_number_mask, account_number, account_number_mask):
    arg_1 = "Visa Platinum 7000 7922 8960 6361"
    ans_1 = "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card(arg_1) == ans_1
    assert mask_account_card(f"Mastercard {card_number}") == f"Mastercard {card_number_mask}"

    argument_2 = "Счет 73654108430135874305"
    answer_2 = "Счет **4305"
    assert mask_account_card(argument_2) == answer_2
    assert mask_account_card(f"Счет {account_number}") == f"Счет {account_number_mask}"

    with pytest.raises(TypeError):
        mask_account_card(0)


def test_get_data():
    argument_3 = '2018-07-11T02:26:18.671407'
    answer_3 = '11.07.2018'

    assert get_data(argument_3) == answer_3

    with pytest.raises(TypeError):
        get_data(0)