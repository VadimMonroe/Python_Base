list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# Генератор тут
# -------------------------------------------------------
print([i for j in range(len(list)) for i in list if i not in list[j + 1:] and i not in list[:j]])

# Обычное решение
# -------------------------------------------------------
new_list = []
count = 0

for i in list:
    if i not in list[count + 1:] and i not in list[:count]:
        new_list.append(i)
    count += 1

print(new_list)


