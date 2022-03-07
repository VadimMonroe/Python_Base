from sys import argv
from itertools import count, cycle

# Вводим переменные для консоли
# Команда в консоли - 'python 4-les-6-dz.py 20 30 40'
# -------------------------------------------------------
script_name, count_number, final_count_number, stop_number_term = argv

# Функция count
# -------------------------------------------------------
def count_func(first_count=10, final_count=15):
    lst = []
    for i in count(first_count):
        if i > final_count:
            break
        else:
            lst.append(i)
    return lst


print(count_func(int(count_number), int(final_count_number)))


# Функция cycle
# -------------------------------------------------------
def cycle_func(stop_number=10):
    lst2 = []
    list = ['null', 1, 'dva']
    i = 0
    for number in cycle(list):
        if i > stop_number:
            break
        else:
            lst2.append(number)
            i += 1
    return lst2


print(cycle_func(int(stop_number_term)))
