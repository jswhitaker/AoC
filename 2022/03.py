def main() -> int:
    with open('inputs/03.txt') as input_file:
        total = 0
        for line in input_file:
            line = line.strip()
            size = len(line)
            assert size % 2 == 0
            first = {item for item in line[:(size // 2)]}
            second = {item for item in line[(size // 2):]}
            common = first.intersection(second)
            assert len(common) == 1
            common_item = common.pop()
            if common_item.islower():
                total += ord(common_item) - ord('a') + 1
            else:
                total += ord(common_item) - ord('A') + 1 + 26
    return total


def main_2() -> int:
    with open('inputs/03.txt') as input_file:
        total = 0
        group = []
        for line in input_file:
            group.append(line.strip())
            if len(group) < 3:
                continue
            first = {item for item in group[0]}
            second = {item for item in group[1]}
            third = {item for item in group[2]}
            common = first & second & third
            assert len(common) == 1
            common_item = common.pop()
            if common_item.islower():
                total += ord(common_item) - ord('a') + 1
            else:
                total += ord(common_item) - ord('A') + 1 + 26
            group = []
    return total


if __name__ == '__main__':
    result = main()
    print(result)
    result = main_2()
    print(result)
