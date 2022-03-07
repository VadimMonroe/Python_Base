class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        income = self._income.values()
        print(f'Зарплата с бонусом: {sum(income)}')


Vasya = Position('Василий', 'Пупкин', 'Столяр', 50000, 20000)
Vasya.get_full_name()
print(Vasya.position)
Vasya.get_total_income()
print('\n')

Petya = Position('Петя', 'Душкин', 'Режиссёр-монтажа', 80000, 30000)
Petya.get_full_name()
print(Petya.position)
Petya.get_total_income()