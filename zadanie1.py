#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Создать класс Triad (тройка чисел); определить методы изменения полей и вычисления
#суммы чисел. Определить производный класс Triangle с полями-сторонами. Определить
#методы вычисления углов и площади треугольника.

# релизовать новый метод класса, для подсчёта углов, данный метод должен вызываться из других методов, в которых это требуется
# добавить if __name__ == "__main__":

import math

class Triad:
    def __init__(self, x=1, y=1, z=1):
        self.x = x
        self.y = y
        self.z = z

    def x_get(self):
        return self.x

    def y_get(self):
        return self.y

    def z_get(self):
        return self.z

    def x_set(self, x):
        self.x = x

    def y_set(self, y):
        self.y = y

    def z_set(self, z):
        self.z = z

    def adxyz(self):
        return self.x + self.y + self.z


class Triangle(Triad):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    @staticmethod
    def calculate_angle(a, b, c):
        # Метод для вычисления угла
        return math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))

    def s(self):
        # Вычисление площади треугольника по формуле Герона
        p = (self.x + self.y + self.z) / 2
        return math.sqrt(p * (p - self.x) * (p - self.y) * (p - self.z))

    def angle_A(self):
        # Вычисление угла A
        return self.calculate_angle(self.x, self.y, self.z)

    def angle_B(self):
        # Вычисление угла B
        return self.calculate_angle(self.y, self.z, self.x)

    def angle_C(self):
        # Вычисление угла C
        return self.calculate_angle(self.z, self.x, self.y)

    def __str__(self):
        return f"x = {self.x};  y = {self.y};  z = {self.z}"


if __name__ == "__main__":
    j = Triangle(25, 23, 35)
    print(f"Площадь треугольника: {j.s()}")
    print(f"x: {j.x_get()}")
    j.y_set(34)
    print(f"Угол A: {j.angle_A()}")
    print(f"Угол B: {j.angle_B()}")
    print(f"Угол C: {j.angle_C()}")
    print(j)
