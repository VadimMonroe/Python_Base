with open('file_to_6_dz.txt', 'r') as f:
    content = f.readlines()
    print(f'Читаем файл: \n{content}\n')

    count = 0
    for i in content:
        count += 1

with open('file_to_6_dz.txt', 'r') as f:
    def func():
        content = f.readline().replace('\n', '')
        list = []
        [list.append(k) for i in content.split(': ') for j in i.split('(') for k in j.split(' ')]
        dict = {}
        dict[list[0]] = sum([int(l) for l in list if l.isdigit()])
        print(dict)
        return dict

    final_lines = func()
    for _ in range(count - 1):
        final_lines = final_lines | func()
    print(f'\nРезультат:\n{final_lines}')
