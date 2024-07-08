from typing import Any, Generator, Iterable


def filter_by_currency(transactions: Iterable[dict], currency: str) -> Generator[dict, Any, None]:
    """Return generator object of transactions with only specific currency."""
    for tr in transactions:
        if tr["operationAmount"]["currency"]["name"] == currency:
            yield tr


def transaction_descriptions(transactions: Iterable[dict]) -> Generator[str, Any, None]:
    """Return generator object of transactions descriptions."""
    for tr in transactions:
        yield tr["description"]


def card_number_generator() -> Generator[str, Any, None]:
    """Return generator object of card numbers in XXXX XXXX XXXX XXXX format."""
    for card_number in range(1, 10 ** 17):
        card = str(card_number).zfill(16)
        card = " ".join((card[start:start + 4] for start in range(0, 16, 4)))
        yield card
