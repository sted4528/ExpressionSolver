from math import sqrt

from Solvers.Solver import Solver


class BiQuadSolver(Solver):
    def __init__(self, args: list):
        self.a = args[0]
        self.a1 = args[1]
        self.b = args[2]
        self.b1 = args[3]
        self.c = args[4]
        self.d = args[5]

    def solve(self) -> list:
        a = self.a
        b = self.b
        c = self.c - self.d
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return []
        elif discriminant == 0:
            return [sqrt(-b / (2 * a))]
        elif discriminant > 0:
            root1 = (-b + sqrt(discriminant)) / (2 * a)
            if root1 > 0:
                new_root1 = sqrt(root1)
            else:
                new_root1 = 'Меньше нуля'
            root2 = (-b - sqrt(discriminant)) / (2 * a)
            if root2 > 0:
                new_root2 = sqrt(root2)
            else:
                new_root2 = 'Меньше нуля'
            return [new_root1, -new_root1, new_root2, -new_root2]
