class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    # Сложение
    def __add__(self, other):
        result = self.quantity + other.quantity
        print(f'Сумма: {result}')
        return result

    # Вычитание
    def __sub__(self, other):
        result = self.quantity - other.quantity
        if result > 0:
            print(f'Разность: {result}')
            return result
        else:
            print('Клеток не может быть меньше 0')

    # Умножение
    def __mul__(self, other):
        result = self.quantity * other.quantity
        print(f'Умножение: {result}')
        return result

    # Деление
    def __truediv__(self, other):
        result = self.quantity // other.quantity
        if result > 0:
            print(f'Деление: {result}')
            return result
        else:
            print(f'При делении нет целых клеток: {result}')

    # Печатаем ячейки
    def make_order(self, quantity_str):
        result = self.quantity // quantity_str
        result_ostatok = self.quantity % quantity_str
        print((('*' * quantity_str) + '\n') * result + ('*' * result_ostatok))

# Назначаем
bug = Cell(1300)
grass = Cell(2300)

# Операции
summa = bug + grass
raznost = bug - grass
proizvedenie = bug * grass
delenie = bug / grass

# Печатаем ячейки
bug.make_order(500)
