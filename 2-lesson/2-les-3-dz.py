n = int(input('Введите число месяца: '))
list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

while True:
    if n > len(list):
        n = int(input('Введите правильное число месяца (всего 12): '))
    else:
        n = n - 1
        print('Введённое Вами число', n + 1, 'соответствует месяцу -', list[n], '(Тут решение реализовано через список.)')
        break

number = input('Введите число месяца: ')
dict = {
    '1': 'Январь',
    '2': 'Февраль',
    '3': 'Март',
    '4': 'Апрель',
    '5': 'Май',
    '6': 'Июнь',
    '7': 'Июль',
    '8': 'Август',
    '9': 'Сентябрь',
    '10': 'Октябрь',
    '11': 'Ноябрь',
    '12': 'Декабрь'
}

print('Введённое Вами число', number, 'соответствует месяцу -', dict[number], '(А здесь решение реализовано через словарь.)')
