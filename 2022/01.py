def main():
    with open('inputs/01.txt') as input_file:
        max_cal = 0
        tmp = 0
        for line in input_file:
            if not line.strip():
                max_cal = max(max_cal, tmp)
                tmp = 0
            else:
                tmp += int(line.strip())
    return max_cal


def main_2():
    with open('inputs/01.txt') as input_file:
        max_cals = [0, 0, 0]
        tmp = 0
        for line in input_file:
            if not line.strip():
                max_cals.append(tmp)
                max_cals.sort(reverse=True)
                del max_cals[-1]
                tmp = 0
            else:
                tmp += int(line.strip())
    return sum(max_cals)


if __name__ == '__main__':
    result = main()
    print(result)
    result = main_2()
    print(result)
