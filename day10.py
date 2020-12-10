import itertools


def part1(data_ints):
    deltas = []
    for i in range(len(data_ints))[1:]:
        deltas.append(data_ints[i] - data_ints[i - 1])
    deltas.sort()
    for k, g in itertools.groupby(deltas):
        print(k)
        print(len(list(g)))
        print('\n')


def part2(data_ints):
    if len(data_ints) == 1:
        return 1
    count = 0
    end = 3 if 3 < len(data_ints) else len(data_ints)
    for i in range(1, end):
        if data_ints[i] - data_ints[0] > 3:
            break
        count += part2(data_ints[i:])
    return count

def part2_better(data_inits):



def main():
    with open('day10-input.txt') as input_file:
        data = input_file.readlines()
    data_ints = [int(d) for d in data]
    data_ints.append(max(data_ints) + 3)
    data_ints.append(0)
    data_ints.sort()
    part1(data_ints)
    print(part2(data_ints))
    return 0


if __name__ == '__main__':
    result = main()
    print(result)
