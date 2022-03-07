# Вариант 1
# -------------------------------------------------------
def int_func(text):
    return ' '.join(i[0].upper() + i[1:] for i in text.split(' '))


print(int_func('odin dva tri chetire pyat'))

# Вариант 2
# -------------------------------------------------------
def int_func2(text):
    return text.title()


print(int_func2('one two three four five'))

# Вариант 3
# -------------------------------------------------------
int_func3 = lambda text: ' '.join(i[0].upper() + i[1:] for i in text.split(' '))
print(int_func3('uno dos tres kvatro'))