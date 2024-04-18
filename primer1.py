#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Rational:
    def __init__(self, a=0, b=1):
        a = int(a)
        b = int(b)
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        self.__numerator = abs(a)
        self.__denominator = abs(b)
        self.__reduce()

    # Сокращение дроби
    def __reduce(self):
        # Функция для нахождения наибольшего общего делителя
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        c = gcd(self.__numerator, self.__denominator)
        self.__numerator //= c
        self.__denominator //= c

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    # Прочитать значение дроби с клавиатуры. Дробь вводится как a/b.
    def read(self, prompt=None):
        line = input(prompt) if prompt is not None else input()
        parts = list(map(int, line.split("/", maxsplit=1)))
        if parts[1] == 0:
            raise ValueError("Denominator cannot be zero.")
        self.__numerator = abs(parts[0])
        self.__denominator = abs(parts[1])
        self.__reduce()

    # Вывести дробь на экран
    def display(self):
        print(f"{self.__numerator}/{self.__denominator}")

    # Сложение обыкновенных дробей.
    def add(self, rhs):
        if isinstance(rhs, Rational):
            a = (
                self.numerator * rhs.denominator
                + self.denominator * rhs.numerator
            )
            b = self.denominator * rhs.denominator
            return Rational(a, b)
        else:
            raise ValueError("Operand must be a Rational.")

    # Вычитание обыкновенных дробей
    def sub(self, rhs):
        if isinstance(rhs, Rational):
            a = (
                self.numerator * rhs.denominator
                - self.denominator * rhs.numerator
            )
            b = self.denominator * rhs.denominator
            return Rational(a, b)
        else:
            raise ValueError("Operand must be a Rational.")

    # Умножение обыкновенных дробей.
    def mul(self, rhs):
        if isinstance(rhs, Rational):
            a = self.numerator * rhs.numerator
            b = self.denominator * rhs.denominator
            return Rational(a, b)
        else:
            raise ValueError("Operand must be a Rational.")

    # Деление обыкновенных дробей.
    def div(self, rhs):
        if isinstance(rhs, Rational):
            a = self.numerator * rhs.denominator
            b = self.denominator * rhs.numerator
            if b == 0:
                raise ValueError("Denominator cannot be zero.")
            return Rational(a, b)
        else:
            raise ValueError("Operand must be a Rational.")

    # Отношение обыкновенных дробей.
    def equals(self, rhs):
        return (
            self.numerator == rhs.numerator
            and self.denominator == rhs.denominator
        )

    def greater(self, rhs):
        return (
            self.numerator / self.denominator > rhs.numerator / rhs.denominator
        )

    def less(self, rhs):
        return (
            self.numerator / self.denominator < rhs.numerator / rhs.denominator
        )


if __name__ == "__main__":
    r1 = Rational(3, 4)
    r1.display()
    r2 = Rational()
    r2.read("Введите обыкновенную дробь: ")
    r2.display()
    r3 = r2.add(r1)
    r3.display()
    r4 = r2.sub(r1)
    r4.display()
    r5 = r2.mul(r1)
    r5.display()
    r6 = r2.div(r1)
    r6.display()
