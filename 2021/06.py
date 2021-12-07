from typing import Dict


def main():
    fish = {}
    with open('inputs/06.txt') as input_file:
        temp_fish = input_file.read().strip().split(',')
    initial_fish = [int(i) for i in temp_fish]
    for i in range(9):
        fish[i] = initial_fish.count(i)

    for i in range(256):
        fish = update_fish(fish)
    return sum(fish.values())


def update_fish(fish: Dict[int, int]):
    new_fish = {}
    for i in range(8, 0, -1):
        new_fish[i-1] = fish[i]
    new_fish[8] = fish[0]
    new_fish[6] = new_fish.get(6, 0) + fish[0]
    return new_fish


if __name__ == '__main__':
    result = main()
    print(result)
