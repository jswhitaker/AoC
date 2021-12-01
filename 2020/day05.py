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
    taken_seats = []
    with open('inputs/05-input.txt') as input_file:
        for line in input_file:
            taken_seats.append(convert(line.strip()))
    taken_seats.sort()
    for i in range(len(taken_seats)):
        if taken_seats[i+1] == taken_seats[i] + 2:
            return taken_seats[i] + 1


if __name__ == '__main__':
    result = main()
    print(result)
