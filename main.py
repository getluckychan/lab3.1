from math import sqrt, pi


class Number:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        print(self.x + self.y)

    def sub(self):
        print(self.x - self.y)


class Real(Number):
    def sqrt(self):
        new_number = sqrt(self.x ** self.y)
        print(new_number)

    def step(self):
        print(pi ** self.x)
        print(pi ** self.y)
