# SkyPro HomeWork

## Описание

Здесь хранятся файлы для домашних заданий в курсе SkyPro Профессия Python-разработчик.

## Установка

1. Клонируйте репозиторий:
    ```
    git clone https://github.com/Mrzillka/SkyPro-Homework.git
    ```

## Использование:

- Файл `src/masks.py` хранит функции из задания №9.1
- Файл `src/widget.py` хранит функции из задания №9.2
- Файл `src/pricessing.py` хранит функции из задания №10.1
- Папка `tests/` хранит модули тестирования из задания №10.2
- Файл `src/generators.py` хранит функции из задания №11.1
- Файл `src/decorators` хранит декоратор из задания №11.2
- Файлы `utils/utils.py` и `utils/external_apy.py` хранят функции из задания №12.1

### Тестирование
Запустите команду `pytest` в консоли

## Документация:

### src

#### masks

##### `get_mask_card_number(card_number: str) -> str`

- Возвращает маску номера карты из 16 символов в формате XXXX XX** **** XXXX

##### `get_mask_account(account_number: str) -> str`

- Возвращает маску 20-значного числа в формате **XXXX

#### processing

##### `filter_by_state(lst_of_dicts: list[dict], state: str = 'EXECUTED') -> list[dict]`

- Возвращает словари с определенным значением ключа state (по умолчанию 'EXECUTED')

##### `sort_by_date(lst_of_dicts: list[dict], is_reverse: bool = True) -> list[dict]`

- Возвращает новый список, содержащий все словари в порядке убывания, отсортированные по значению даты.

#### widget

##### `mask_account_card(type_and_number: str) -> str`

- Получает тип и номер карты/счета и возвращает строку с замаскированным номером.

##### `get_data(full_time: str) -> str`

- Возвращает дату в формате ДД.ММ.ГГГГ

#### generators

##### `filter_by_currency(transactions: Iterable[dict], currency: str) -> Generator[dict, Any, None]`

- Возвращает объект-генератор транзакций только с определенной валютой.

##### `transaction_descriptions(transactions: Iterable[dict]) -> Generator[str, Any, None]`

- Возвращает объект-генератор описаний транзакций.

##### `card_number_generator() -> Generator[str, Any, None]`

- Возвращает объект-генератор номеров карт в формате XXXX XXXX XXXX XXXX.

#### decorators

##### `log(filename: Optional[str] = None) -> Any | None`

- Логгирует корректность работы функции в файл (в консоль по умолчанию)

### utils

#### utils

##### `get_transactions_from_json(path: str) -> Any`

- Читает все транзакции из файла JSON и возвращает dict

#### external_api

##### `convert_to_rub(amount: float, _form: str) -> float`

- Конвертирует сумму валюты из любой в RUB

##### `get_transaction_amount(transaction: dict) -> float`

- Возвращает суммы операции в рублях

## Лицензия:

Этот проект лицензирован по [лицензии MIT](https://ru.wikipedia.org/wiki/Лицензия_MIT).
