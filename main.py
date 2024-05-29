from Entities.Parser import Parser
from Entities.ParserSolverAdapter import solving

#print(Parser.parse_expression("2x^2 - 0x + 3 = -10"))
# print(Parser.parse_expression("2x^2 - 0x + 13 = 0"))
# print(Parser.parse_expression("2x^2 - 10x + 3 = -10 + 10x + x^2"))
# print(solving("x^4 - 4x^2 + 4 = 0"))
#print(Parser.parse_expression("10 - 1x2 = 15x + 15"))
# print(Expression(Parser.get_solving("2x^2 - 0x + 13 = 0")).solve())
# print(Expression([1, 0, -4, 0, 4, 0]).solve())
# print(Expression([1, -1, 10, 0]).solve())
# print(Expression([2, 25, 10]).solve())
# print(Expression([1, 0, 4, 0, 4, 0]).solve())
# print(Expression([1, 0, -5, 0, -36, 0]).solve())  # Д == 0, 2 корень
# print(Expression([1, 0, -5, 0, 6, 0]).solve())  # Д > 0, 4 корня
# print(Expression([1, 0, -1, 0, 10, 0]).solve())  # Д < 0, 0 корней
# print(solving("x4 - 5x2 + 6 = 0")) # Д < 0, 0 корней
#print(solving("2x^2 - 10x + 3 = -10 + 10x + x^2"))
#print(solving("10 - 0x2 = 15 + 15x")) # не понимает  минус перед х2, ошибка если в конце выражения переменная х
                                        # работает если ставим перед х2 число(0 или 1)
print(solving("10 - 1x2 = 15x + 15"))
print(Parser.parse_expression("10 - x2 = 15x + 15"))
# print(solving("2x - 6 = 0"))
