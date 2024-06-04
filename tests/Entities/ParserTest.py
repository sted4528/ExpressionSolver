import pytest
from Entities.Parser import Parser


class TestParser:
    # FISH: For cloning
    def test_simple(self):
        # arrange
        # act
        # assert
        assert True

    def test_one_token_linear_negative(self):
        # arrange
        expression_str = "-x = 0"
        sut = Parser
        truth = [(-1.0, 'x', 1.0)], []
        # act
        result = sut.parse_expression(expression_str)
        # assert
        assert result == truth

    def test_one_token_quad(self):
        # arrange
        expression_str = "x2 = 0"
        sut = Parser
        truth = [(1.0, 'x', 2.0)], []
        # act
        result = sut.parse_expression(expression_str)
        # assert
        assert result == truth

    def test_two_token_quad_end_const(self):
        # arrange
        expression_str = "x2 + 15 = 0"
        sut = Parser
        truth = [(1.0, 'x', 2.0), (15.0, '', 0)], []
        # act
        result = sut.parse_expression(expression_str)
        # assert
        assert result == truth

    def test_two_token_quad_end_linear(self):
        # arrange
        expression_str = "x2 + 15x = 0"
        sut = Parser
        truth = [(1.0, 'x', 2.0), (15.0, 'x', 1)], []
        # act
        result = sut.parse_expression(expression_str)
        # assert
        assert result == truth

    def test_two_token_quad_end_linear_right_const(self):
        # arrange
        expression_str = "x2 + 15x = -3"
        sut = Parser
        truth = [(1.0, 'x', 2.0), (15.0, 'x', 1)], [(-3.0, '', 0)]
        # act
        result = sut.parse_expression(expression_str)
        # assert
        assert result == truth

    # TODO: Exception!!!
    def test_two_token_quad_end_linear_right_linear(self):
        # arrange
        expression_str = "x2 + 15x = -3x"
        sut = Parser
        truth = [(1.0, 'x', 2.0), (15.0, 'x', 1)], [(-3.0, 'x', 1)]
        # act
        result = sut.parse_expression(expression_str)
        # assert
        assert result == truth

    def test_two_token_quad_end_linear_right_quad(self):
        # arrange
        expression_str = "x2 + 15x = -3x2"
        sut = Parser
        truth = [(1.0, 'x', 2.0), (15.0, 'x', 1)], [(-3.0, 'x', 2)]
        # act
        result = sut.parse_expression(expression_str)
        # assert
        assert result == truth
