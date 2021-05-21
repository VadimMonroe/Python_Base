import json

with open('file_to_7_dz.txt', 'r') as f:
    content = f.readlines()
    print(f'Читаем файл: \n{content}\n')

    # Счётчик кол-ва фирм
    # -------------------------------------------------------
    count_firms = 0
    for i in content:
        count_firms += 1

with open('file_to_7_dz.txt', 'r') as f:
    # Функция рассчёта прибыли или убытка для каждой фирмы
    # -------------------------------------------------------
    def func():
        content = f.readline().replace('\n', '')
        print(f'{content}\n', end='')
        list = []
        [list.append(i) for i in content.split(' ')]
        sum = int(list[2]) - int(list[3])
        print(f'Прибыль - {list[0]}: {sum}\n')
        dict = {}
        dict[list[0]] = sum
        return dict


    # Создаём словарь из фирм
    # -------------------------------------------------------
    final_lst = func()
    for _ in range(count_firms - 1):
        final_lst = final_lst | func()

    # Высчитываем сколько фирм с прибылями, сколько с убытками
    # -------------------------------------------------------
    count_for_ap = count_for_al = average_profit = average_loss = 0
    for val in final_lst.values():
        if val >= 0:
            count_for_ap += 1
            average_profit = (average_profit + val) / count_for_ap
        else:
            count_for_al += 1
            average_loss = (average_loss + val) / count_for_al

    dict_average_profit = dict(average_profit=average_profit)
    dict_average_loss = dict(average_loss=average_loss)
    final_lst = [final_lst, dict_average_profit, dict_average_loss]

    print('Средняя прибыль фирм: ', average_profit)
    print(f'\nРезультат:\n{final_lst}')

# Создаём json файл и сохраняем инфу в него
# -------------------------------------------------------
with open('5-les-7-dz.jon', 'w') as f_jon:
    json.dump(final_lst, f_jon)

with open('5-les-7-dz.jon', 'r') as f_jon1:
    json_final_lst = json.load(f_jon1)
    print(f'Распечатка из Jsona: \n{json_final_lst}')