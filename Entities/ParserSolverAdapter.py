from Entities.Expression import Expression
from Entities.Parser import Parser


def solving(expression: str):
    monomials_all = Parser.parse_expression(expression)
    x4, x2, x, non_x = 0, 0, 0, 0
    for item in monomials_all:
        for j in item:
            # print(j[0], j[1], j[2])
            if j[2] == 4.0:
                x4 += j[0]
            if j[2] == 2.0:
                x2 += j[0]
            if j[2] == 1:
                x += j[0]
            if j[2] == 0:
                non_x += j[0]
    if x4 == 0:
        if x2 != 0:
            coefficient_list = [x2, x, non_x, 0]
        if x2 == 0:
            coefficient_list = [x, non_x, 0]
    else:
        coefficient_list = [x4, 0, x2, 0, non_x, 0]
    result_solving = Expression(coefficient_list).solve()
    return result_solving
