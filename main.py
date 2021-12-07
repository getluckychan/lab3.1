from math import sqrt, pi
from sys import exit


class Number():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y


class Real(Number):
    def sqrt(self, other):
        return pow(self.x, 1 / float(other))

    def step(self):
        return pi ** self.x, pi ** self.y
