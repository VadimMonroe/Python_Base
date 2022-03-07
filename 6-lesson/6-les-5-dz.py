class Stationery:
    def __init__(self, title):
        self.title = title


    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def draw(self):
        print('Начинаем писать ручкой!')


class Pencil(Stationery):
    def draw(self):
        print('Начинаем рисовать карандашом!')


class Handle(Stationery):
    def draw(self):
        print('Подчёркиваем текст')


blue_pen = Stationery('Синяя Ручка')
red_pen = Pen('Красная Ручка')
black_pencil = Pencil('Чёрный Карандаш')
red_handle = Handle('Красный Маркер')

print(blue_pen.title)
print(red_pen.title)
print(black_pencil.title)
print(red_handle.title, '\n')


blue_pen.draw()
red_pen.draw()
black_pencil.draw()
red_handle.draw()
