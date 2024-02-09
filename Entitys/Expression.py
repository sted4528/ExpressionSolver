from Solvers.BiQuadSolver import BiQuadSolver
from Solvers.LinearSolver import LinearSolver
from Solvers.QuadSolver import QuadSolver
from Solvers.Solver import Solver


class Expression:
    def __init__(self, coefficients: list):
        coefficients_count = len(coefficients)
        if coefficients_count == 3:
            self.solver: Solver = LinearSolver(coefficients)
        elif coefficients_count == 4:
            self.solver: Solver = QuadSolver(coefficients)
        elif coefficients_count == 6:
            self.solver: Solver = BiQuadSolver(coefficients)
        else:
            self.solver: Solver = Solver()

    def solve(self):
        return self.solver.solve()
