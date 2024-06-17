# SkyPro HomeWork

## Описание

Здесь хранятся файлы для домашних заданий в курсе SkyPro Профессия Python-разработчик.

## Установка

1. Клонируйте репозиторий:
    ```
    git clone https://github.com/username/project-x.git
    ```

## Использование:

- Файл `src/masks.py` хранит функции для маскировки номера карты и счета пользователя.
- Файлs `src/widget.py` и `src/pricessing.py` хранит дополнительные функции

## Документация:

### masks

#### `get_mask_card_number(card_number: str) -> str`

- Возвращает маску номера карты из 16 символов в формате XXXX XX** **** XXXX

#### `get_mask_account(account_number: str) -> str`

- Возвращает маску 20-значного числа в формате **XXXX

### processing

#### `filter_by_state(lst_of_dicts: list[dict], state: str = 'EXECUTED') -> list[dict]`

- Возвращает словари с определенным значением ключа state (по умолчанию 'EXECUTED')

#### `sort_by_date(lst_of_dicts: list[dict], is_reverse: bool = True) -> list[dict]`

- Возвращает новый список, содержащий все словари в порядке убывания, отсортированные по значению даты.

### widget

#### `mask_account_card(type_and_number: str) -> str`

- Получает тип и номер карты/счета и возвращает строку с замаскированным номером.

#### `get_data(full_time: str) -> str`

- Возвращает дату в формате ДД.ММ.ГГГГ

## Лицензия:

Этот проект лицензирован по [лицензии MIT](https://ru.wikipedia.org/wiki/Лицензия_MIT).
