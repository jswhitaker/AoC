def main_2():
    lines = []
    with open('inputs/03.txt') as input_file:
        for line in input_file:
            lines.append(line.strip())

    o_rating = ''
    co_rating = ''
    o_lines = lines.copy()
    co_lines = lines.copy()

    while len(o_lines) > 1:
        o_rating, o_lines = air_rating(o_lines, True, o_rating)

    while len(co_lines) > 1:
        co_rating, co_lines = air_rating(co_lines, False, co_rating)

    return int(o_lines[0], 2) * int(co_lines[0], 2)

def air_rating(lines, is_most, prefix):
    count = 0
    for val in lines:
        count += int(val[len(prefix)])
    if count >= (len(lines) / 2):
        prefix += '1' if is_most else '0'
    else:
        prefix += '0' if is_most else '1'

    return prefix, [entry for entry in lines if entry[:len(prefix)] == prefix]


def main():
    with open('inputs/03.txt') as input_file:
        digits = [0] * 12
        for line in input_file:
            for i, v in enumerate(line.strip()):
                digits[i] += int(v)

        bin_gamma = '0b'
        bin_eps = '0b'
        for d in digits:
            if d > 500:
                bin_gamma += '1'
                bin_eps += '0'
            else:
                bin_gamma += '0'
                bin_eps += '1'
        return int(bin_gamma, 2) * int(bin_eps, 2)


if __name__ == '__main__':
    result = main_2()
    print(result)
