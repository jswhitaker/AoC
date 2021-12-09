import functools
import itertools
from typing import List, Dict, Set, Tuple


def main():
    rows = []
    with open('inputs/09.txt') as input_file:
        for line in input_file:
            rows.append([int(x) for x in line.strip()])
    width = len(rows[0]) + 2
    for i, r in enumerate(rows):
        rows[i] = [9] + r + [9]
    rows.insert(0, [9] * width)
    rows.append([9] * width)
    task_1_points = task_1(rows)
    return task_2(rows)


def task_1(rows):
    low_points = []
    for y in range(1, len(rows) - 1):
        for x in range(1, len(rows[0]) - 1):
            val = rows[y][x]
            if val < rows[y-1][x] and val < rows[y+1][x] and val < rows[y][x-1] and val < rows[y][x+1]:
                low_points.append(val)
    return low_points


def task_2(rows):
    basins = []
    low_points = find_low_points(rows)
    for l_point in low_points:
        to_check = [l_point]
        checked = set()
        while len(to_check) > 0:
            x, y = to_check.pop()
            checked.add((x, y))
            new_points = []
            for x_2, y_2 in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if rows[y_2][x_2] < 9 and ((x_2, y_2) not in checked):
                    new_points.append((x_2, y_2))
            to_check.extend(new_points)
        basins.append(len(checked))
    return functools.reduce(lambda a, b: a*b, sorted(basins, reverse=True)[:3])


def find_low_points(rows: List[List[int]]) -> List[Tuple[int, int]]:
    low_points = []
    for y in range(1, len(rows) - 1):
        for x in range(1, len(rows[0]) - 1):
            val = rows[y][x]
            if val < rows[y - 1][x] and val < rows[y + 1][x] and val < rows[y][x - 1] and val < rows[y][x + 1]:
                low_points.append((x, y))
    return low_points


if __name__ == '__main__':
    result = main()
    print(result)
