import pytest
from Entities.ParserSolverAdapter import solving
from Entities.Parser import Parser

class TestSolver:
    @pytest.mark.parametrize(
        "expression, result",
        [
            ("10 - 1x2 = 15x + 15", ([(10.0, '', 0), (-1.0, 'x', 2.0)], [(-15.0, 'x', 1), (-15.0, '', 0)])),
            ("10 - x2 = 15x + 15", ([(10.0, '', 0), (-0.0, 'x', 2.0)], [(-15.0, 'x', 1), (-15.0, '', 0)])),
            ("10 - x2 = 15 + 15x", ([(10.0, '', 0), (-0.0, 'x', 2.0)], [(-15.0, '', 0), (-15.0, 'x', 1)])),
            ("2x^2 - 10x + 3 = -10 + 10x + x^2", ([(2.0, 'x', 2.0), (-10.0, 'x', 1), (3.0, '', 0)], [(10.0, '', 0), (-10.0, 'x', 1), (-1, 'x', 2.0)]))
        ]
    )

    def test_parse(self, expression, result):
        assert Parser.parse_expression(expression) == result


    @pytest.mark.parametrize(
        "expression, result",
        [
            ("x^4 - 4x^2 + 4 = 0",[(2 ** 0.5), (-2 ** 0.5)]),
            ("2x^2 - 10x + 13 = 0",[(2.5 + 0.5j), (2.5 - 0.5j)]),
            ("2x - 6 = 0", [3]),
            ("2x^2 - 10x + 3 = -10 + 10x + x^2", [(19.327379053088816), (0.6726209469111843)]), # как сделать чтобы работало для 19.3 и 0.67
            ("x4 - 5x2 - 36 = 0", [(3 + 0j), (-3 - 0j), (2j), (-2j)])
        ]
    )
    def test_solving(self, expression, result):
        assert solving(expression) == result
