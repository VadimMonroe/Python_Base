class OfficeEquipment:
    """Офисные приналежности"""
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def run(self):
        print(f'Названиe: {self.name}, Количество: {self.quantity}, Цена: {self.cost}')
        print(f'Запускаем устройство! {self.name}')


class Printer(OfficeEquipment):
    cost = 100


class Scanner(OfficeEquipment):
    cost = 80


class Xerox(OfficeEquipment):
    cost = 150


class Warehouse:
    """Весь склад"""
    def __init__(self):
        self.printer = Printer('Принтер', 30)
        self.scanner = Scanner('Сканнер', 20)
        self.xerox = Xerox('Ксерокс', 10)

    @property
    def start(self):
        self.printer.run()
        self.scanner.run()
        self.xerox.run()

    def start_income(self):
        while True:
            new_items = input(
                'Введите что должно поступить на склад (в формате: имя, кол-во, цена, подразделение, название): (Для окончания введите "end"): ')
            if new_items != "end":
                list = []
                list.append(new_items.split())
                try:
                    list[0][1] = int(list[0][1])
                    list[0][2] = int(list[0][2])
                    wildberries.__income(list)
                except:
                    print('Неверно введены значения! Введите заного!')

            else:
                break

    def __income(self, income_dict):
        income_dict1 = {'Название': income_dict[0][4], 'Имя': income_dict[0][0], 'Кол-во': income_dict[0][1],
                        'Цена': income_dict[0][2], 'Подразделение': income_dict[0][3]}

        print(income_dict1)

        with open('base_equipment.txt', 'a') as f:
            print(income_dict1, file=f)


wildberries = Warehouse()
wildberries.start
wildberries.start_income()
