from typing import List, Tuple


def main():
    steps = []
    with open('inputs/02.txt') as input_file:
        for line in input_file:
            steps.append(line.split())
    return part2(steps)

def part1(steps: List[Tuple[str, str]]):
    depth = 0
    horz = 0
    for direction, num in steps:
        if direction == 'forward':
            horz = horz + int(num)
        elif direction == 'down':
            depth = depth + int(num)
        elif direction == 'up':
            depth = depth - int(num)
    return depth * horz

def part2(steps: List[Tuple[str, str]]):
    aim = 0
    depth = 0
    horz = 0
    for direction, num in steps:
        if direction == 'forward':
            horz = horz + int(num)
            depth = depth + (aim * int(num))
        elif direction == 'down':
            aim = aim + int(num)
        elif direction == 'up':
            aim = aim - int(num)
    return depth * horz

if __name__ == '__main__':
    result = main()
    print(result)
