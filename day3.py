def main(right, down):
    position = 0
    trees = 0
    with open('day3-input.txt') as input_file:
        for i, line in enumerate(input_file):
            if i % down != 0:
                continue
            line = line.strip()
            if line[position % len(line)] == '#':
                trees += 1
            position += right
    return trees


if __name__ == '__main__':
    result = 1
    result *= main(1, 1)
    result *= main(3, 1)
    result *= main(5, 1)
    result *= main(7, 1)
    result *= main(1, 2)
    print(result)

