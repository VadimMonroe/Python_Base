class Road:
    def __init__(self, length, width, mass, weight):
        self._length = length
        self._width = width
        self._mass = mass
        self._weight = weight

    def result(self):
        result = self._length * self._width * self._mass * self._weight
        value = 'кг.'
        if result >= 1000:
            result = result // 1000
            value = 'т.'

        print(f'{result} {value} - масса асфальта, необходимого для покрытия всего дорожного полотна.')

road_calculation = Road(20, 3000, int(input('Введите массу, в кг: ')), int(input('Введите толщину, в см: ')))

road_calculation.result()