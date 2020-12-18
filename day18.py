from typing import Optional, List, Tuple


class Calculator(object):
    current_value: Optional[int]
    prev_operator: Optional[str]
    equation: List[str]

    def __init__(self, equation: List[str]):
        self.equation = equation
        self.prev_operator = None
        self.current_value = None

    @classmethod
    def from_str(cls, equation_str: str):
        return cls(equation_str.split())

    # Part 1
    def solve(self) -> Tuple[int, int]:
        i = 0
        while i < len(self.equation):
            obj = self.equation[i]
            if obj.isdecimal():
                self.do_math(int(obj))
            elif obj in ['+', '*']:
                self.prev_operator = obj
            elif obj == '(':
                inner_cal = Calculator(self.equation[i + 1:])
                inner_i, inner_solution = inner_cal.solve()
                self.do_math(inner_solution)
                # Plus 1 to account for opening parentheses
                i += inner_i + 1
            elif obj == ')':
                break
            i += 1
        return i, self.current_value

    # This assumes parens are the highest always.
    def solve_with_precedence(self, operations: List[str]) -> Tuple[int, int]:
        length = 0
        while '(' in self.equation and self.equation.index('(') < self.equation.index(')'):
            next_paren = self.equation.index('(')
            inner_cal = Calculator(self.equation[next_paren + 1:])
            inner_len, inner_solution = inner_cal.solve_with_precedence(operations)
            new_eq = self.equation[:next_paren] + [str(inner_solution)] + self.equation[next_paren + inner_len + 2:]
            # Only add 1 since the new value `inner_solution` replaces one of the 2 parens.
            length += inner_len + 1
            self.equation = new_eq
        if ')' in self.equation:
            closing_paren = self.equation.index(')')
            self.equation = self.equation[:closing_paren]
        length += len(self.equation)
        for op in operations:
            self.__resolve_operation(op)
        return length, self.current_value

    def __resolve_operation(self, operation: str):
        new_eq = []
        for obj in self.equation:
            if obj.isdecimal():
                self.do_math(int(obj))
            elif obj == operation:
                self.prev_operator = obj
            elif obj == ')':
                break
            else:
                new_eq.append(str(self.current_value))
                new_eq.append(obj)
                self.current_value = None
                self.prev_operator = None
        new_eq.append(str(self.current_value))
        self.equation = new_eq

    def do_math(self, val: int):
        if self.prev_operator == '+':
            self.current_value += val
            self.prev_operator = None
        elif self.prev_operator == '*':
            self.current_value *= val
            self.prev_operator = None
        else:
            self.current_value = val


def main():
    total_sum_1 = 0
    total_sum_2 = 0
    with open('inputs/18-input.txt') as input_file:
        for line in input_file:
            if line.startswith('#'):
                continue
            line = line.replace('(', '( ')
            line = line.replace(')', ' )')
            calc_1 = Calculator.from_str(line)
            _, value_1 = calc_1.solve()
            calc_2 = Calculator.from_str(line)
            _, value_2 = calc_2.solve_with_precedence(['+', '*'])
            total_sum_1 += value_1
            total_sum_2 += value_2
    print('Part 1: ', total_sum_1)
    print('Part 2: ', total_sum_2)
    return 0


if __name__ == '__main__':
    result = main()
    print(result)
