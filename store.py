class Store:
    def __init__(self, address, name, items):
        self.address = address
        self.name = name
        self.items = items

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            return "Товар удален"
        return "Товар не найден"

    def get_price(self, name):
        if name not in self.items:
            return None
        return self.items[name]

    def edit_item_price(self, name, new_price):
        if name in self.items:
            if new_price < 0:
                return "Цена не может быть отрицательная"
            self.items[name] = new_price
            return "Цена обновлена"
        return "Товар не найден"

    def get_all_items(self, show_header=True):
        if show_header:
            print("\n-----------------------")
            print(f"Товары в магазине {self.name}:")
        # Исправлено: используем list(self.items.keys()) для корректной индексации
        for index, item in enumerate(list(self.items.keys()), 1):
            print(f"{index}. {item}: {self.items[item]} руб.")
        if show_header:
            print("-----------------------\n")


stores = []

store1 = Store("ул. Пушкина", "Магазин №1", {})
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)
store1.add_item("вишня", 1)
stores.append(store1)

store2 = Store("ул. Лермонтова", "Магазин №2", {})
store2.add_item("груша", 0.5)
store2.add_item("киви", 0.75)
store2.add_item("слива", 1)
stores.append(store2)

store3 = Store("ул. Ленина", "Магазин №3", {})
store3.add_item("персик", 0.5)
store3.add_item("апельсин", 0.75)
store3.add_item("мандарин", 1)
stores.append(store3)


def display_stores():
    print("Управление товарами в магазинах. Выберите магазин")
    for index, store in enumerate(stores, 1):
        print(f"{index}. {store.name} Адрес: {store.address}")


def get_valid_store_choice(max_index):
    """Получает и проверяет выбор магазина."""
    while True:
        try:
            choice = input("Введите номер магазина или 0 для выхода: ")
            choice_int = int(choice)
            if choice_int == 0:
                return None
            if 1 <= choice_int <= max_index:
                return choice_int - 1
            print(f"Ошибка: введите число от 1 до {max_index} или 0")
        except ValueError:
            print("Ошибка: введите корректное число")


def get_valid_action():
    """Получает и проверяет выбор действия."""
    while True:
        print("-----------------------")
        print("Введите действие:")
        print("1. Добавить товар")
        print("2. Редактировать цену товара")
        print("3. Удалить товар")
        print("0. Выход")
        print("-----------------------")
        action = input("Введите номер действия: ")
        if action in ["0", "1", "2", "3"]:
            return action
        print("Неверное действие")


# Основной цикл
while True:
    display_stores()
    store_index = get_valid_store_choice(len(stores))
    if store_index is None:
        break

    store = stores[store_index]
    store.get_all_items()

    while True:
        action = get_valid_action()
        if action == "0":
            break

        if action == "1":
            name = input("Введите название товара: ")
            try:
                price = float(input("Введите цену: "))
                store.add_item(name, price)
                store.get_all_items()
            except ValueError:
                print("Ошибка: введите корректную цену (число)")

        elif action == "2":
            try:
                item_num = int(input("Введите номер товара для редактирования цены: "))
                if 1 <= item_num <= len(store.items):
                    try:
                        new_price = float(input("Введите новую цену: "))
                        result = store.edit_item_price(
                            list(store.items.keys())[item_num - 1], new_price
                        )
                        print(result)
                        store.get_all_items()
                    except ValueError:
                        print("Ошибка: введите корректную цену (число)")
                else:
                    print("Неверный номер товара")
            except ValueError:
                print("Ошибка: введите корректный номер товара")

        elif action == "3":
            try:
                item_num = int(input("Введите номер товара для удаления: "))
                if 1 <= item_num <= len(store.items):
                    result = store.remove_item(list(store.items.keys())[item_num - 1])
                    print(result)
                    store.get_all_items()
                else:
                    print("Неверный номер товара")
            except ValueError:
                print("Ошибка: введите корректный номер товара")
