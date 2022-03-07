def my_func(x, y, z):
    """
    Сортируем переменные по величине в списке и прибавляем наибольшие числа по индексам;
    x, y, z должны быть числами;
    Проверка на ошибку, если введена строка.
    """
    list = [x, y, z]
    try:
        result = sorted(list)[::-1][0] + sorted(list)[::-1][1]
        print(result)
        return result
    except TypeError:
        print('Ошибка')

my_func(3.5, 99.4, 5)
