import itertools
from typing import Tuple, List


def main():
    vents = []
    with open('inputs/05.txt') as input_file:
        for line in input_file:
            points = line.strip().split(' -> ')
            start_pos = points[0].split(',')
            end_pos = points[1].split(',')
            vents.append(((int(start_pos[0]), int(start_pos[1])), (int(end_pos[0]), int(end_pos[1]))))
    v_map = make_map(vents)
    return v_map


def make_map(vents: List[Tuple[Tuple[int, int], Tuple[int, int]]]):
    x_max = 0
    y_max = 0
    for ((x_1, y_1), (x_2, y_2)) in vents:
        x_max = max(x_max, x_1, x_2)
        y_max = max(y_max, y_1, y_2)
    v_map = [[0 for _ in range(x_max + 1)] for _ in range(y_max + 1)]
    for ((x_1, y_1), (x_2, y_2)) in vents:
        if x_1 == x_2 or y_1 == y_2:
            for x in (range(x_1, x_2+1)) if x_1 < x_2 else range(x_2, x_1+1):
                for y in (range(y_1, y_2+1)) if y_1 < y_2 else range(y_2, y_1+1):
                    v_map[y][x] = v_map[y][x] + 1
        elif abs(x_1 - x_2) == abs(y_1 - y_2):
            x_list = list(range(x_1, x_2+1)) if x_1 < x_2 else list(range(x_1, x_2-1, -1))
            y_list = list(range(y_1, y_2+1)) if y_1 < y_2 else list(range(y_1, y_2-1, -1))
            points = zip(x_list, y_list)
            for x, y in points:
                v_map[y][x] = v_map[y][x] + 1
    return v_map


if __name__ == '__main__':
    result = main()
    for line in result:
        print(line)
    count = 0
    for i in result:
        for j in i:
            if j > 1:
                count += 1
    print(count)
