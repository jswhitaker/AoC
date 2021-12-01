from typing import List


def main():
    depths = []
    with open('inputs/01.txt') as input_file:
        for line in input_file:
            depths.append(int(line))
    return depth_increases(depths, 1), depth_increases(depths, 3)


def depth_increases(depths: List[int], length: int):
    deeper = 0
    for i in range(len(depths) - length):
        if depths[i + length] > depths[i]:
            deeper = deeper + 1
    return deeper


if __name__ == '__main__':
    result = main()
    print(result)
