# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

sec = int(input('Введите число, которое нужно преобразовать в часы и минуты: '))

h = int(sec // 3600)
m= int(sec / 60 % 60)
s = sec % 60

print('Ваш результат (чч:мм:сс): {:02}:{:02}:{:02}'.format(h ,m, s))
print(f'Ваш результат (чч:мм:сс): {h:02}:{m:02}:{s:02}')