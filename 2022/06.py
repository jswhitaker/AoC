def main() -> int:
    with open('inputs/06.txt') as input_file:
        for line in input_file:
            for i in range(14, len(line)):
                test = set(line[i - 14:i])
                if len(test) == 14:
                    return i


if __name__ == '__main__':
    result = main()
    print(result)
