from random import randint

my_list = []

for n in range(10):
    my_list.append(randint(1, 100))

my_list = sorted(my_list)[::-1]
print(my_list)

number = int(input('Введите число: '))
i = 0
while my_list[i] > number:
    if i + 1 == len(my_list):
        my_list.append(number)
        break
    i += 1
else:
    my_list.insert(i, number)

print(my_list)