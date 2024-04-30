from math import sqrt
import cmath

from Solvers.QuadSolver import QuadSolver
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
        roots = QuadSolver([self.a, self.b, self.c, self.d]).solve()
        if len(roots) == 2:
            root1_positive = cmath.sqrt(roots[0])
            root1_negative = -cmath.sqrt(roots[0])
            root2_positive = cmath.sqrt(roots[1])
            root2_negative = -cmath.sqrt(roots[1])
            return [root1_positive, root1_negative, root2_positive, root2_negative]
        if len(roots) == 1:
            return [cmath.sqrt(roots[0]),-cmath.sqrt(roots[0])]
        if len(roots) == 0:
            return []
