import numpy as np
import sympy as sp

class Base:
    def __init__(self, x1, y1, w1):
        self.x = x1
        self.y = y1
        self.w = w1

    def distance(self, other):

        dist = np.sqrt((self.x - other.x) ** 2 + ((self.y - other.y) ** 2))

        return float(dist)

    def is_attacked(self, rocket):

        dist = ((self.x - rocket.x) ** 2 + ((self.y - rocket.y) ** 2))
        if dist <= rocket.r**2:
            return True
        else:
            return False

    def get_centres(self, other, r):
        a1 = int(self.x)
        b1 = int(self.y)
        a2 = int(other.x)
        b2 = int(other.y)
        x, y = sp.symbols('x,y', real=True)
        f1 = sp.Eq((a1 - x) ** 2 + (b1 - y) ** 2 - r ** 2, 0)
        f2 = sp.Eq((a2 - x) ** 2 + (b2 - y) ** 2 - r ** 2, 0)
        return sp.solve([f1, f2])
