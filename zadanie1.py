import math
# создать метод класса и реалтзовать внутри math.sqrt(p * (p - self.x) * (p - self.y) * (p - self.z))

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

    def s(self):
        p = (self.x + self.y + self.z) / 2
        return math.sqrt(p * (p - self.x) * (p - self.y) * (p - self.z))

    def angle_A(self):
        a, b, c = self.x, self.y, self.z
        return math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))

    def angle_B(self):
        a, b, c = self.x, self.y, self.z
        return math.degrees(math.acos((c**2 + a**2 - b**2) / (2 * c * a)))

    def angle_C(self):
        a, b, c = self.x, self.y, self.z
        return math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))

    def __str__(self):
        return f"x = {self.x};  y = {self.y};  z={self.z}"


j = Triangle(25, 23, 35)
print(j.s())
print(j.x_get())
j.y_set(34)
print(j.angle_A())
print(j.angle_B())
print(j.angle_C())
print(j)
