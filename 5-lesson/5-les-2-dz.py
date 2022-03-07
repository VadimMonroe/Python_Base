# Универсальный вариант
# -------------------------------------------------------
with open('file_to_2_dz.txt', 'r') as f:
    count = 0
    for line in f:
        count += 1
        print(f'Строка в текстовом документе: {line}')
        print('Кол-во слов в строке:', len(line.split(' ')))
        print('Кол-во букв в строке', len(line))
        print('*' * 100)
    print(f'Всего кол-во строк {count}')

with open('file_to_2_dz.txt', 'r') as f:
    print('Общее кол-во букв:', len(f.read()))

# Отдельный вариант подсчёта строк
# -------------------------------------------------------
with open('file_to_2_dz.txt', 'r') as f:
    print('\nКол-во строк:', len(f.readlines()))