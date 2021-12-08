from typing import List, Dict, Set, Tuple


def main():
    o_lines = []
    dig_o_lines = []
    with open('inputs/08.txt') as input_file:
        for line in input_file:
            in_out = line.split('|')
            patterns = in_out[0].strip().split()
            output = in_out[1].strip().split()
            o_lines.append(output)
            dig_o_lines.append((patterns, output))
    return task_1(o_lines), task_2(dig_o_lines)


def task_1(o_lines: List[List[str]]) -> int:
    count = 0
    for l in o_lines:
        for o in l:
            if len(o) in [2, 3, 4, 7]:
                count += 1
    return count


def task_2(dig_o_lines: List[Tuple[List[str], List[str]]]) -> int:
    total = 0
    for line in dig_o_lines:
        seg_map = determine_digits(line[0])
        rev_map = {''.join(sorted(v)): k for k, v in seg_map.items()}
        val = 0
        for i, o in enumerate(line[1]):
            val = (val*10) + rev_map[''.join(sorted(o))]
        total += val
    return total


def determine_digits(digits: List[str]) -> Dict[int, Set[str]]:
    # noinspection PyDictCreation
    seg_map = {}
    seg_map[1] = find_one(digits)
    seg_map[4] = find_four(digits)
    seg_map[7] = find_seven(digits)
    seg_map[8] = find_eight(digits)
    seg_map.update(find_zero_six_nine(digits, seg_map[1], seg_map[4]))
    seg_map.update(find_two_three_five(digits, seg_map[1], seg_map[4]))
    return seg_map


def find_one(digits: List[str]) -> Set[str]:
    for d in digits:
        if len(d) == 2:
            return set(d)


def find_seven(digits: List[str]) -> Set[str]:
    for d in digits:
        if len(d) == 3:
            return set(d)


def find_four(digits: List[str]) -> Set[str]:
    for d in digits:
        if len(d) == 4:
            return set(d)


def find_eight(digits: List[str]) -> Set[str]:
    for d in digits:
        if len(d) == 7:
            return set(d)


def find_two_three_five(digits: List[str], one: Set[str], four: Set[str]) -> Dict[int, Set[str]]:
    results = {}
    pos = [set(d) for d in digits if len(d) == 5]
    for p in pos:
        if one.issubset(p):
            results[3] = p
        elif (four - one).issubset(p):
            results[5] = set(p)
        else:
            results[2] = set(p)
    return results


def find_zero_six_nine(digits: List[str], one: Set[str], four: Set[str]) -> Dict[int, Set[str]]:
    results = {}
    pos = [set(d) for d in digits if len(d) == 6]
    for p in pos:
        if not one.issubset(p):
            results[6] = p
        elif four.issubset(p):
            results[9] = p
        else:
            results[0] = p
    return results


if __name__ == '__main__':
    result = main()
    print(result)
