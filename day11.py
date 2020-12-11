from typing import Dict, List, Optional, Callable


def print_seating(seating: Dict[int, List[Optional[bool]]]):
    for rows in seating.values():
        row = ''
        for s in rows:
            if s is None:
                row += '.'
            elif not s:
                row += 'L'
            else:
                row += '#'
        print(row)


class SeatingArea(object):
    def __init__(self, seating, max_adj):
        self.seating = seating
        self.max_adj = max_adj
        self.new_seating = {}
        self.seating_change_count = 0

    def check_adjacent(self, row: int, col: int) -> int:
        occupied_count = 0
        adj = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
               (row, col - 1), (row, col + 1),
               (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
        for r, c in adj:
            try:
                occupied_count += 1 if c >= 0 and self.seating[r][c] else 0
            except (IndexError, KeyError):
                pass
        return occupied_count

    def check_adjacent_seats(self, row: int, col: int) -> int:
        occupied_count = 0
        adj_shifts = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        for r, c in adj_shifts:
            r_modifier = r
            c_modifier = c
            try:
                while (col + c_modifier) >= 0 and self.seating[row + r_modifier][col + c_modifier] is None:
                    r_modifier += r
                    c_modifier += c
                occupied_count += 1 if (col + c_modifier) >= 0 and self.seating[row + r_modifier][col + c_modifier] else 0
            except (IndexError, KeyError):
                pass
        return occupied_count

    def update_seating(self, adj_method: Callable[[int, int], int]):
        for r, seats in self.seating.items():
            self.new_seating[r] = []
            for s, seat in enumerate(seats):
                if self.seating[r][s] is None:
                    self.new_seating[r].append(None)
                elif seat and adj_method(r, s) > self.max_adj:
                    self.new_seating[r].append(False)
                elif not seat and adj_method(r, s) == 0:
                    self.new_seating[r].append(True)
                else:
                    self.new_seating[r].append(seat)

    def find_seating_balance(self) -> int:
        balanced = False
        while not balanced:
            self.update_seating(self.check_adjacent_seats)
            self.seating_change_count += 1
            print(self.seating_change_count)
            print_seating(self.new_seating)
            balanced = self.new_seating == self.seating
            self.seating = self.new_seating.copy()
            self.new_seating = {}
        occupied_count = 0
        for row in self.seating.values():
            for seat in row:
                occupied_count += 1 if seat else 0
        # print_seating(self.seating)
        return occupied_count


def main() -> int:
    # Dict of key = row, value = seat in row
    seating_dict = {}
    with open('inputs/11-input.txt') as input_file:
        for r, row in enumerate(input_file):
            seating_dict[r] = []
            for seat in row.rstrip():
                if seat == 'L':
                    seating_dict[r].append(False)
                elif seat == '#':
                    seating_dict[r].append(True)
                else:
                    seating_dict[r].append(None)
    seating_area = SeatingArea(seating_dict, 4)
    return seating_area.find_seating_balance()


if __name__ == '__main__':
    result = main()
    print(result)
