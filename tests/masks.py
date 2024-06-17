from src.masks import get_mask_card_number, get_mask_account


# Пример работы функции, возвращающей маску карты
argument_1 = '7000792289606361'     # входной аргумент
answer_1 = '7000 79** **** 6361'  # выход функции
assert get_mask_card_number(argument_1) == answer_1

# Пример работы функции, возвращающей маску счета
argument_2 = '73654108430135874305'  # входной аргумент
answer_2 = '**4305'  # выход функции
assert get_mask_account(argument_2) == answer_2
