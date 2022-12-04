def main() -> int:
    with open('inputs/04.txt') as input_file:
        total = 0
        for line in input_file:
            line = line.strip()
            range_a, range_b = line.split(',')
            range_a_start, range_a_end = (int(x) for x in range_a.split('-'))
            range_b_start, range_b_end = (int(x) for x in range_b.split('-'))
            if (range_a_start <= range_b_start and range_a_end >= range_b_end) or \
                (range_b_start <= range_a_start and range_b_end >= range_a_end):
                total += 1
    return total


def main_2() -> int:
    with open('inputs/04.txt') as input_file:
        total = 0
        for line in input_file:
            line = line.strip()
            range_a, range_b = line.split(',')
            range_a_start, range_a_end = (int(x) for x in range_a.split('-'))
            range_b_start, range_b_end = (int(x) for x in range_b.split('-'))
            if (range_a_start <= range_b_start <= range_a_end) or \
                (range_b_start <= range_a_start <= range_b_end):
                total += 1
    return total


if __name__ == '__main__':
    result = main()
    print(result)
    result = main_2()
    print(result)
