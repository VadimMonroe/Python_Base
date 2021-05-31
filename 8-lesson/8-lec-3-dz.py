class CrushListCheck(Exception):
    def __init__(self, txt):
        self.txt = txt


class CheckList:
    def __init__(self, lst):
        for i in lst.split():
            try:
                i = int(i)
                new_lst.append(i)
                print(new_lst)
            except Exception:
                print(CrushListCheck('У Вас в списке присутствует строка!'))


new_lst = []
list = []
while True:
    number = input('Введите число для заполнения списка (Для окончания введите "end"): ')
    if number != "end":
        list = ''.join(number)
        check_check = CheckList(list)
    else:
        print('Финальный список:', new_lst)
        break
