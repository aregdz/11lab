# добавить raise для исключений (12, 20, 24)
# добавить пере. операторов
from abc import ABC, abstractmethod


class Pair(ABC):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def subtract(self, other):
        pass

    @abstractmethod
    def multiply(self, other):
        pass

    @abstractmethod
    def divide(self, other):
        pass


class FuzzyNumber(Pair):
    def add(self, other):
        return FuzzyNumber(self.first + other.first, self.second + other.second)

    def subtract(self, other):
        return FuzzyNumber(self.first - other.first, self.second - other.second)

    def multiply(self, other):
        return FuzzyNumber(self.first * other.first, self.second * other.second)

    def divide(self, other):
        return FuzzyNumber(self.first / other.first, self.second / other.second)


class ComplexNumber(Pair):
    def add(self, other):
        return ComplexNumber(
            self.first + other.first, self.second + other.second
        )

    def subtract(self, other):
        return ComplexNumber(
            self.first - other.first, self.second - other.second
        )

    def multiply(self, other):
        return ComplexNumber(
            self.first * other.first - self.second * other.second,
            self.first * other.second + self.second * other.first,
        )

    def divide(self, other):
        denominator = other.first**2 + other.second**2
        real = (
            self.first * other.first + self.second * other.second
        ) / denominator
        imaginary = (
            self.second * other.first - self.first * other.second
        ) / denominator
        return ComplexNumber(real, imaginary)


fuzzy1 = FuzzyNumber(3, 0.1)
fuzzy2 = FuzzyNumber(5, 0.2)
fuzzy_sum = fuzzy1.add(fuzzy2)
print("Прстые числа:", fuzzy_sum.first, fuzzy_sum.second)

complex1 = ComplexNumber(2, 3)
complex2 = ComplexNumber(1, -1)
complex_product = complex1.multiply(complex2)
print(
    "Комплексные числа:",
    complex_product.first,
    "+",
    complex_product.second,
    "i",
)
