from abc import ABC, abstractmethod


class Сlothes(ABC):
    @abstractmethod
    def calculate(self):
        pass

    # @abstractmethod
    # def my_method_2(self):
    #     pass


class Сoat(Сlothes):
    def __init__(self, V):
        self.__V = V

    @property
    def calculate(self):
        return round(self.__V/6.5 + 0.5, 2)


class Suit(Сlothes):
    def __init__(self, H):
        self.__H = H

    @property
    def calculate(self):
        return round(2 * self.__H + 0.3, 2)


test_1 = Сoat(1)
test_2 = Suit(1)
print(test_1.calculate)
print(test_2.calculate)