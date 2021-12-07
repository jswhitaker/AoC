import statistics
from functools import cache

from parse import *
from typing import Dict


def main():
    crabs = []
    with open('inputs/07.txt') as input_file:
        temp_crabs = input_file.read().strip().split(',')
    crabs = [int(i) for i in temp_crabs]
    med = statistics.median(crabs)
    print(statistics.mean(crabs))
    fuel = 0
    for c in crabs:
        fuel += abs(med-c)
    return fuel


def main_2():
    crabs = []
    with open('inputs/07.txt') as input_file:
        temp_crabs = input_file.read().strip().split(',')
    crabs = [int(i) for i in temp_crabs]
    c_max = max(crabs)
    c_min = min(crabs)
    min_fuel = None
    min_pos = -1
    for i in range (c_min, c_max+1):
        curr_fuel = 0
        for c_pos in crabs:
            curr_fuel += fuel_cost(c_pos, i)
        if min_fuel is None:
            min_fuel = curr_fuel
            min_pos = i
        elif curr_fuel < min_fuel:
            min_fuel = curr_fuel
            min_pos = i
    return min_pos, min_fuel


@cache
def fuel_cost(c_pos, final_pos):
    return sum(range(0, abs(c_pos - final_pos) + 1))


if __name__ == '__main__':
    result = main_2()
    print(result)