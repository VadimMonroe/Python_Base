# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

plus = int(input('Введите значение выручки фирмы: '))
minus = int(input('Введите значение издержек фирмы: '))

result = plus - abs(minus)

if plus - minus < 0:
        print('Фирма отработала с убытком: ', result)
else:
        print("Фирма отработала с прибылью: ", result)
        viruchka_result = result / plus * 100
        print('Соотношение прибыли к выручке: ', viruchka_result)
        people = int(input('Введите количество сотрудников: '))
        plus_result = result // people
        print('Прибыль фирмы на каждого сотрудника составляет: ', plus_result)