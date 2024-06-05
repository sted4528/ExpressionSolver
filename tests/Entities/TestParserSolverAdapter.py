from Entities.ParserSolverAdapter import solving


class TestParserSolverAdapter:
    # FISH: For cloning
    def test_simple(self):
        # arrange
        # act
        # assert
        assert True

    def test_two_roots_equal(self):
        # (x-1)*(x-1) = 0
        # x^2 - 2x + 1 = 0
        # arrange
        experssion = "x^2 - 2x + 1 = 0"
        truth = [1.0]
        # act
        result = solving(experssion)
        # assert
        assert result == truth

