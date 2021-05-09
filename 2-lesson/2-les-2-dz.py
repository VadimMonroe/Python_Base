list = []

while True:
    number = input('Введите число для заполнения списка (Для окончания введите "end"): ')
    if number == "end":
        break
    else:
        list.append(int(number))

print(f'Оригинальный список: {list}')
iteration = int(len(list))//2
i = 0
for variation in range(iteration):
    list[i], list[i + 1] = list[i + 1], list [i]
    i += 2

print(f'Список с перевёрнутыми числами: {list}')
