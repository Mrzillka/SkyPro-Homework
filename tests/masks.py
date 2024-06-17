from src.masks import get_mask_card_number, get_mask_account


# Пример работы функции, возвращающей маску карты
arg_1 = '7000792289606361'     # входной аргумент
ans_1 = '7000 79** **** 6361'  # выход функции
assert get_mask_card_number(arg_1) == ans_1

# Пример работы функции, возвращающей маску счета
arg_2 = '73654108430135874305'  # входной аргумент
ans_2 = '**4305'  # выход функции
assert get_mask_account(arg_2) == ans_2
