from typing import Optional, List, Tuple


class ExpenseReport(object):

    def __init__(self, expense_list: List[int]):
        self.expense_list = expense_list

    def expense2(self, goal2: int, index) -> Optional[Tuple[int, int]]:
        for e in self.expense_list[index:]:
            other = goal2 - e
            if other in self.expense_list[index:]:
                return e, other
            else:
                continue
        return None

    def expense3(self, goal3: int):
        for i, e in enumerate(self.expense_list):
            remainder = goal3 - e
            try:
                e2, e3 = self.expense2(remainder, i + 1)
            except TypeError:
                continue
            return e, e2, e3


if __name__ == '__main__':
    expenses: list[int] = list()
    with open('inputs/01-input.txt') as expense_file:
        for expense in expense_file:
            expenses.append(int(expense))
    expenses.sort()
    report: ExpenseReport = ExpenseReport(expenses)
    print(report.expense3(2020))
