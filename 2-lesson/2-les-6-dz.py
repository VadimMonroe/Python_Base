products = []

count = 1
user_count = int(input('Введите количество товаров: '))

while count <= user_count:
    name = input('Введите имя товара: ')
    price = input('Введите цену товара: ')
    number = input('Введите кол-во товара: ')
    izm = input('Введите единицу измерения: ')

    products.append((count, {
        'Название': name,
        'Цена': price,
        'Кол-во': number,
        'Ед.': izm
    }))
    count += 1

print(products)

analitic = {
    'Названий': [],
    'Цен': [],
    'Кол-во': [],
    'Ед.': []
}

for key, value in products:
    analitic['Названий'].append(value['Название'])
    analitic['Цен'].append(value['Цена'])
    analitic['Кол-во'].append(value['Кол-во'])
    analitic['Ед.'].append(value['Ед.'])

print('Аналитика о товарах: ', analitic)
