
from Entitys.Expression import Expression
from Entitys.Parser import Parser


print(Parser.parse_expression("2x^2 - 0x + 3 = -10"))
print(Parser.parse_expression("2x^2 - 10x + 3 = -10 + 10x + x^2"))

print(Expression([3, -3, 0]).solve())
print(Expression([2, 4, 5, 10]).solve())
print(Expression([1, 0, -5, 0, 5, 0]).solve())