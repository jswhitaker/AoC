def convert(code):
    bin_code = 0b0
    for char in code:
        bin_code *= 0b10
        if char in ['B', 'R']:
            bin_code += 0b1
    return bin_code


def main():
    max_code = 'FFFFFFFLLL'
    max_bin = convert(max_code)
    with open('day5-input.txt') as input_file:
        for line in input_file:
            new_bin = convert(line.strip())
            if new_bin > max_bin:
                max_bin = new_bin
                max_code = line.strip()
    return max_code


if __name__ == '__main__':
    result = main()
    print('max code:' + result + ' ' + str(convert(result)) + ' ' + bin(convert(result)))
