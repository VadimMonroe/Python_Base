n = input('Введите несколько слов через пробел: ')
n = n.split(" ")
print(n)

for num, i in enumerate(n):
    print(f'{num + 1}. {i[:10]}')