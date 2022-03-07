class ComplexNumber:
    def __init__(self, znachenie):
        self.znachenie = znachenie

    def __add__(self, other):
        return self.znachenie ** other.znachenie
        # (a + bj) + (c + dj) = (a + c) + (b + d)j

    def __mul__(self, other):
        return self.znachenie / other.znachenie
        # (a + bj) + (c + dj) = ac + bcj + adj + bd**j = (ac + bd**j) + (bc + ad)j = (ac - bd) + (bc + ad)j


a = ComplexNumber(2 + 3j)
b = ComplexNumber(1 - 4j)

sum_result = a + b
sum_result_real = a.znachenie + b.znachenie

mul_result = a * b
mul_result_real = a.znachenie * b.znachenie


print('Перегруженное значение суммы: ', sum_result)
print('Реальное значение суммы: ', sum_result_real, '\n')
print('Перегруженное значение произведения: ', mul_result)
print('Реальное значение произведения: ', mul_result_real)
