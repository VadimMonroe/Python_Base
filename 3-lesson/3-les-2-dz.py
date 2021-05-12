def people(**kwargs):
    """Вводимые аргументы: name, second_name, birth_date, city, email, tel"""
    print(kwargs, end='\n\n')

    # Реализовать вывод данных о пользователе одной строкой:
    for key, val in kwargs.items():
        print(f'{key} - {val}', end='; ')


people(name='Franko', second_name='Батитучи', birth_date='07.12.2020',
       city='Moscow', email='prop@mail.ru', tel='89998887766')
