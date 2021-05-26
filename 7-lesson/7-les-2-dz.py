from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def result(self):
        coat = self.size / 6.5 + 0.5
        print(f'Затраты ткани на Пальто: {coat}')
        return coat



class Costume(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def result(self):
        costume = 2 * self.height + 0.3
        print(f'Затраты на ткань костюма: {costume}')
        return costume

super_palto = Coat('Пальто', 32)
super_costume = Coat('Костюм', 180)

print(f'Общие затраты ткани: {super_palto.result + super_costume.result}')
