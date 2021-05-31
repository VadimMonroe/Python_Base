class Data:
    def __init__(self, date):
        self.date = date


    @classmethod
    def my_func(cls, date):
        lst = [int(i) for i in date.split('-')]
        print(cls, lst)
        return lst


    @staticmethod
    def validation_month(lst):
        if lst[1] > 12:
            print('В году 12 месяцев, Вы ошиблись!')
        else:
            print('Всё норм!')

Data.my_func("30-05-2020")

data_class = Data("30-05-2020")
data_class.my_func("30-05-2020")

Data.validation_month(Data.my_func("30-05-2020"))
data_class.validation_month(Data.my_func("30-05-2020"))
