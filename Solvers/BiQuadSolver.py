from math import sqrt

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
        roots = QuadSolver.solve(self)
        if len(roots) == 2:
            root1_positive = sqrt(roots[0]) if roots[0] > 0 else []
            root1_negative = -sqrt(roots[0]) if roots[0] > 0 else []
            root2_positive = sqrt(roots[1]) if roots[1] > 0 else []
            root2_negative = -sqrt(roots[1]) if roots[1] > 0 else []
            return [root1_positive, root1_negative, root2_positive, root2_negative]
        if len(roots) == 1:
            return [sqrt(roots[0])]
        if len(roots) == 0:
            return []
