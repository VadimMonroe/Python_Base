# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

input_number = input('Введите целое положительное число (для того, чтобы, мы вычислили самую большую цифру в числе: ')

while True:
    try:
        length = len(input_number)
        number = int(input_number)
        i = 0
        max_number = 0
        while i <= length:
            input_number = number // (10 ** (length - i))
            if input_number > max_number:
                max_number = input_number
            number = number % (10 ** (length - i))
            i += 1
        print(f'Наибольшая цифра {max_number}.')
        break

    except ValueError:
        input_number = input('Вы ввели неверное значение, введите цифру: ')

