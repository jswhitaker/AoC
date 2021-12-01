import itertools


#1309761972

def decrypt(target):
    sum_num = []
    with open('inputs/09-input.txt') as input_file:
        data = input_file.readlines()
    for line in data:
        print(sum(sum_num))
        print('Delta: ' + str(target - sum(sum_num)))
        if sum(sum_num) == target:
            print('found: ' + str(sum_num))
            min_num = min(sum_num)
            max_num = max(sum_num)
            return min_num, max_num
        elif sum(sum_num) < target:
            print('Below')
            sum_num.append(int(line))
        else:
            while sum(sum_num) > target:
                sum_num.pop(0)
                if sum(sum_num) == target:
                    print('found: ' + str(sum_num))
                    min_num = min(sum_num)
                    max_num = max(sum_num)
                    return min_num, max_num
            sum_num.append(int(line))
    min_num = min(sum_num)
    max_num = max(sum_num)
    return min_num, max_num

def decrypt_brute(target):
    with open('inputs/09-input.txt') as input_file:
        data = input_file.readlines()
    data_int = [int(k) for k in data]
    for i in range(len(data)):
        for j in range(len(data))[i:]:
            if sum(data_int[i:j]) == target:
                return min(data_int[i:j]), max(data_int[i:j])
    return None


def invalid_number():
    sum_num = []
    with open('inputs/09-input.txt') as input_file:
        data = input_file.readlines()
    for line in data[:25]:
        sum_num.append(int(line))
    for line in data[25:]:
        if int(line) not in [i + j for i, j in itertools.combinations(sum_num, 2)]:
            return line
        else:
            sum_num.pop(0)
            sum_num.append(int(line))


def main ():
    i, j = decrypt(1309761972)
    return i + j


if __name__ == '__main__':
    result = main()
    print(result)
