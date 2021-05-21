with open('file_to_1_dz.txt', 'w') as f:
    x = None
    count = 1
    while not x == ' ':
        x = input(f'Введите значение для записи в строку № {count} (для остановки ПРОБЕЛ): ')
        print(x, file=f)
        count += 1