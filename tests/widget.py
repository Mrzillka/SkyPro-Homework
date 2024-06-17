from src.widget import mask_account_card, get_data

# Пример для карты
arg_1 = "Visa Platinum 7000 7922 8960 6361"  # входной аргумент
ans_1 = "Visa Platinum 7000 79** **** 6361"  # выход функции

assert mask_account_card(arg_1) == ans_1

# Пример для счета
arg_2 = "Счет 73654108430135874305"  # входной аргумент
ans_2 = "Счет **4305"  # выход функции

assert mask_account_card(arg_2) == ans_2

arg_3 = '2018-07-11T02:26:18.671407'
ans_3 = '11.07.2018'

assert get_data(arg_3) == ans_3
