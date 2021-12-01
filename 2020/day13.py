import itertools
from sympy.ntheory.modular import crt

def part1():
    with open('inputs/13-input.txt') as input_file:
        data = input_file.readlines()
    ts = int(data[0])
    routes = data[1].rstrip().split(',')
    routes = itertools.filterfalse(lambda r: r == 'x', routes)
    routes = [int(r) for r in routes]
    min_route = None
    min_wait = 100000000000000000000000000
    for r in routes:
        wait = 0 if ts % r == 0 else r - (ts % r)
        if wait < min_wait:
            min_wait = wait
            min_route = r
    print(min_wait)
    print(min_route)
    return min_route * min_wait


def part2():
    with open('inputs/13-input.txt') as input_file:
        data = input_file.readlines()
    ts = int(data[0])
    routes = data[1].rstrip().split(',')
    route_offset = {}
    for i, r in enumerate(routes):
        if r != 'x':
            route_offset[int(r)] = i
    print(route_offset)
    print(route_offset.keys())
    print(route_offset.values())
    print(crt(route_offset.keys(), [-v for v in route_offset.values()], check=False))
    return 0


def main():
    return part2()


if __name__ == '__main__':
    result = main()
    print(result)
