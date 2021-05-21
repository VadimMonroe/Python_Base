import time


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Скорость, {self.name} - {self.speed}')

    def go(self):
        print(f'Машина, {self.name}, поехала')

    def stop(self):
        print(f'Машина, {self.name}, остановилась')

    def turn(self, direction):
        if direction == 'left':
            print(f'Машина, {self.name}, повернула налево.')
        elif direction == 'right':
            print(f'Машина, {self.name}, повернула направо.')
        else:
            print('Введите left или right')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name}, превышает!!!!')
        else:
            print(f'Скорость, {self.name} - {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name}, превышает!!!!')
        else:
            print(f'Скорость, {self.name} - {self.speed}')


class SportCar(Car):
    def more_speed(self):
        self.speed = 200


class PoliceCar(Car):
    def migalka(self):
        for i in range(2, 0, -1):
            print('Полицейская Мигалка красная')
            time.sleep(1)
            print('Полицейская Мигалка синяя')
            time.sleep(1)

    def arrest(self, name):
        print(f'{name}, Вы арестованы Полицией!')

# Назначаем персонажей
# -----------------------------------------------------------
ferrari_car = SportCar(190, 'red', 'Ferrari', False)
police_supercar = PoliceCar(120, 'black&white', 'Police_Dodge', True)
dyadya_fedya_car = TownCar(70, 'blue', 'Zaz', False)
vasya_goforawork = WorkCar(50, 'yellow', 'bmw', False)

# Запускаем процессы
# -----------------------------------------------------------
ferrari_car.go()
print(ferrari_car.speed)
ferrari_car.more_speed()
ferrari_car.show_speed()
ferrari_car.speed = 220
ferrari_car.show_speed()

# Превышение
# -----------------------------------------------------------
dyadya_fedya_car.go()
dyadya_fedya_car.show_speed()

# Выехала Полиция
# -----------------------------------------------------------
police_supercar.go()
police_supercar.migalka()

dyadya_fedya_car.turn('left')
police_supercar.turn('left')

dyadya_fedya_car.turn('right')
police_supercar.turn('right')

# Арест!
# -----------------------------------------------------------
police_supercar.arrest(dyadya_fedya_car.name)

vasya_goforawork.go()
vasya_goforawork.show_speed()
vasya_goforawork.speed = 40
vasya_goforawork.show_speed()
