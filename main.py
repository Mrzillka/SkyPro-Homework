from src import utils, processing, widget, generators


def main():
    """Main function of project"""
    transactions = None
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("Выберете необходимый пункт в меню:")
        print("1. Получить информацию от транзакциях из JSON-файла")
        print("2. Получить информацию от транзакциях из CSV-файла")
        print("3. Получить информацию от транзакциях из XLSX-файла")
        answer = input()
        if answer == "1":
            print("Для обработки выбран JSON-файл.")
            transactions = utils.get_transactions("data/operations.json")
        elif answer == "2":
            print("Для обработки выбран CSV-файл.")
            transactions = utils.get_transactions("data/operations.json")
        elif answer == "3":
            print("Для обработки выбран XLSX-файл.")
            transactions = utils.get_transactions("data/operations.json")
        else:
            print("Такого пункта нет!")
            continue
        break

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input().upper().strip()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = processing.filter_by_state(transactions, status)
        else:
            print(f"Статус операции \"{status}\" недоступен.")
            continue
        print(f"Операции отфильтрованы по статусу \"{status}\"")
        break

    while True:
        is_sort_by_date = input(
            "Отсортировать операции по дате? Да/Нет\n").lower().strip()
        if is_sort_by_date == "да":
            while True:
                is_sort_ascending = input(
                    "Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию\n").lower().strip()
                if is_sort_ascending == "по возрастанию":
                    transactions = processing.sort_by_date(transactions, False)
                    break
                elif is_sort_ascending == "по убыванию":
                    transactions = processing.sort_by_date(transactions, True)
                    break
                else:
                    print("Введите только \"по возрастанию\" или \"по убыванию\"")
        elif is_sort_by_date == "нет":
            break
        else:
            print("Введите только \"да\" или \"нет\"")
            continue
        break

    while True:
        is_only_rub = input("Выводить только рублевые тразакции? Да/Нет\n").lower().strip()
        if is_only_rub == "да":
            transactions = list(generators.filter_by_currency(transactions, "RUB"))
            break
        elif is_only_rub == "нет":
            break
        else:
            print("Введите только \"да\" или \"нет\"")

    while True:
        is_only_rub = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower().strip()
        if is_only_rub == "да":
            word = input("Введите слово: ")
            transactions = processing.filter_by_description(transactions, word)
            break
        elif is_only_rub == "нет":
            break
        else:
            print("Введите только \"да\" или \"нет\"")

    print("Распечатываю итоговый список транзакций...\n")
    if len(transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return
    print(f"Всего банковских операций в выборке: {len(transactions)}\n")
    for transaction in transactions:
        print(f"{widget.get_data(transaction['date'])} {transaction['description'][:]}")
        print(widget.mask_account_card(transaction['to']))
        print(f"Сумма: {transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}")
        print()


if __name__ == '__main__':
    main()
