#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать абстрактный базовый класс Pair с виртуальными арифметическими операциями.
# Создать производные классы FazzyNumber (нечеткое число) и Complex (комплексное число).

# релизовать новый метод класса, для подсчёта углов, данный метод должен вызываться из других методов, в которых это требуется
# добавить if __name__ == "__main__":
# НЕОБЯЗАТЕЛЬНОЕ УСЛОВИЕ: последнюю строку реализовать через f-строку

from abc import ABC, abstractmethod


class Pair(ABC):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    @abstractmethod
    def add(self, other):
        raise NotImplementedError("Этот метод должен быть переопределён в подклассе")

    @abstractmethod
    def subtract(self, other):
        raise NotImplementedError("Этот метод должен быть переопределён в подклассе")

    @abstractmethod
    def multiply(self, other):
        raise NotImplementedError("Этот метод должен быть переопределён в подклассе")

    @abstractmethod
    def divide(self, other):
        raise NotImplementedError("Этот метод должен быть переопределён в подклассе")


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

if __name__ == "__main__":
    fuzzy1 = FuzzyNumber(3, 0.1)
    fuzzy2 = FuzzyNumber(5, 0.2)
    fuzzy_sum = fuzzy1.add(fuzzy2)
    print("Прстые числа:", fuzzy_sum.first, fuzzy_sum.second)

    complex1 = ComplexNumber(2, 3)
    complex2 = ComplexNumber(1, -1)
    complex_product = complex1.multiply(complex2)
    
    print(f"Комплексные числа: {complex_product.first} + {complex_product.second}i")
