from Solvers.Solver import Solver


class LinearSolver(Solver):
    # ax + b = c
    def __init__(self, args: list):
        self.a = args[0]
        self.b = args[1]
        self.c = args[2]

    # ax + b = c
    # x = (c - b) / a
    def solve(self) -> list:
        if self.a != 0:
            x = (self.c - self.b) / self.a
            return [x]
        else:
            return [self.b == self.c]
