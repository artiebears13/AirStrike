import numpy as np
import sympy as sp




class Rocket():
    def __init__(self, r, x_center, y_center, damage):
        self.r = r
        self.x = x_center
        self.y = y_center
        self.w = damage

    def check_belonging(self, x, y):
        return (x - self.x) ** 2 + (y - self.y) ** 2 < self.r ** 2

    def add_target(self, w):
        self.w += w

    def get_damage(self, targets):
        for i in targets:

            if i.is_attacked(self):
                self.add_target(i.w)
