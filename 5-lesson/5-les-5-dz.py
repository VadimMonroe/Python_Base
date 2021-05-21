with open('file_to_5_dz.txt', 'w') as f:
    print(input('Введите числа, через пробел: '), file=f)

with open('file_to_5_dz.txt', 'r') as f:
    content = f.read()
    print(f'Печатаем цифры из файла: {content}')
    summ = 0
    for i in content.split(' '):
        if i.isdigit():
            summ = summ + int(i)

    print(summ)