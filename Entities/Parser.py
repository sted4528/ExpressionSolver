from Entities.Expression import Expression


class Parser:
    # "-3.1415x"
    # "3x^2 - 10x + 5 = 10"

    @staticmethod
    def parse_expression(line: str):  # expression - выражение

        expression = line.replace(" ", "")  # удаляем все пробелы в строке

        monomials_left = []  # создаем список для хранения результатов
        monomials_right = []
        is_equal_find = False
        while len(expression) != 0:  # при помощи цикла получаем число, переменную, степень и оставшуюся строку

            cur_is_eq, expression = Parser.equal_find(expression)  # если нашли "=" меняем знак
            if cur_is_eq:
                is_equal_find = True

            factor, variable, exp, expression = Parser.__parse_mono__(expression)
            if is_equal_find:
                monomials_right.append((-factor, variable, exp))
            else:
                monomials_left.append((factor, variable, exp))  # добавляем число,переменную,степень в список кортежем
        return monomials_left, monomials_right

    @staticmethod
    def equal_find(line: str):  # ищем равно чтобы отделить левую часть от правой

        if line[0] == '=':
            return True, line[1:]
        else:
            return False, line

    @staticmethod
    def __parse_mono__(line: str) -> (float, str, float, str, bool):  # "->" явно указывает получаемый тип

        expression = line

        number, expression = Parser.__parse_number__(expression)  # получаем число и обрезанное выражение из метода
        # = 5
        #   ^->
        if len(expression) == 0:
            return number, "", 0, ""
        # 5+9
        #  ^
        if not (expression[0].isalpha() or expression[0] == "*"):
            return number, "", 0, expression
        variable, expression = Parser.__parse_variable__(expression)
        exponent, expression = Parser.__parse_exponent__(expression)

        return number, variable, exponent, expression

    # *xuy...
    # xuy...
    @staticmethod
    def __parse_variable__(line: str) -> (str, str):

        cur_pos: int = 0
        variable_str: str = ''

        if line[0] == '*':
            cur_pos += 1

        for i in range(cur_pos, len(line)):
            if line[cur_pos].isalpha():
                variable_str += line[cur_pos]
                cur_pos += 1
            else:
                break
        return variable_str, line[cur_pos:]

    @staticmethod
    def __parse_exponent__(line: str) -> (float, str):

        cur_pos: int = 0
        if line[0] == '^':
            cur_pos += 1
        elif line[0] != '^' and not line[0].isdigit():
            return 1, line

        return Parser.__parse_number__(line[cur_pos:])

    @staticmethod
    def __parse_number__(line: str) -> (float, str):

        cur_pos: int = 0
        number_str: str = ""

        # "-3.1415"
        #  ^
        if line[0] == '-':
            number_str = line[0]
            cur_pos += 1
        elif line[0] == '+':
            number_str = line[0]
            cur_pos += 1

        if not line[cur_pos].isdigit():
            return 1, line[cur_pos:]

        # "-31.1415"
        #   ^^
        for i in range(cur_pos, len(line)):
            if line[i].isdigit():
                number_str = number_str + line[i]
                cur_pos += 1
            else:
                break

        # "-31x"
        #     x
        if cur_pos == len(line) or line[cur_pos] != '.':
            return float(number_str), line[cur_pos:]

        # "-31.1415"
        #     ^
        number_str = number_str + line[cur_pos]
        cur_pos += 1

        # "-31.1415"
        #      ^^^^
        for i in range(cur_pos, len(line)):
            if line[i].isdigit():
                number_str = number_str + line[i]
                cur_pos += 1
            else:
                break

        return float(number_str), line[cur_pos:]
