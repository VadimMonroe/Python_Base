class DivisionZero(Exception):
    def __init__(self, txt):
        self.txt = txt


a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))


class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def solution(self):
        try:
            if b == 0:
                raise DivisionZero('На ноль делить низя!')
            else:
                result = a / b
                print('Ваш результат:', result)
        except DivisionZero:
            result = a
            print('Т.к. делитель ничего не сделал, делимое осталось прежним', result)
        return result


reshenie = Example(a, b)
reshenie.solution
