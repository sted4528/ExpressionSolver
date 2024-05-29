from math import sqrt
import cmath

from Solvers.Solver import Solver


class QuadSolver(Solver):
    def __init__(self, args: list):
        self.a = args[0]
        self.b = args[1]
        self.c = args[2]
        self.d = args[3]

    def solve(self) -> list:
        a = self.a
        b = self.b
        c = self.c - self.d
        discriminant = b**2 - 4 * a * c
        if discriminant < 0:
            return [(-b + cmath.sqrt(discriminant))/(2 * a), (-b - cmath.sqrt(discriminant))/(2 * a)]
        elif discriminant == 0:
            return [-b / (2 * a)]
        elif discriminant > 0:
            return [(-b + cmath.sqrt(discriminant)) / (2 * a), (-b - cmath.sqrt(discriminant)) / (2 * a)]
