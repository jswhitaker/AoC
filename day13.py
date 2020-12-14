import itertools


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
    pass


def main():
    return part2()


if __name__ == '__main__':
    result = main()
    print(result)
