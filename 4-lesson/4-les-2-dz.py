list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# Вариант 1 обычный
# -------------------------------------------------------
def my_func(input_list):
    lst_not_generator = []
    for el in range(len(list)-1):
        if input_list[el] < input_list[el+1]:
            lst_not_generator.append(input_list[el+1])
    return lst_not_generator

print(my_func(list))

# Вариант 2 генератор
# -------------------------------------------------------
lst_generator = [list[el+1] for el in range(len(list)-1) if list[el] < list[el+1]]
print(lst_generator)
