from itertools import cycle
from typing import List


class Cups(object):
    cups: str

    def __init__(self, cups: str):
        self.cups = cups
        self.current_cup = cups[0]

    def do_move(self):
        curr_cup_index = self.cups.index(self.current_cup)
        temp_cup_list = self.cups[curr_cup_index:] + self.cups[:curr_cup_index]
        moving_cups = temp_cup_list[1:4]
        temp_cup_list = temp_cup_list[0] + temp_cup_list[4:]
        dest_cup = next_cup(self.current_cup)
        while dest_cup not in temp_cup_list:
            dest_cup = next_cup(dest_cup)
        dest_cup_index = temp_cup_list.index(dest_cup)
        temp_cup_list = temp_cup_list[:dest_cup_index + 1] + moving_cups + temp_cup_list[dest_cup_index + 1:]
        self.cups = temp_cup_list
        self.current_cup = temp_cup_list[(temp_cup_list.index(self.current_cup) + 1) % 9]


def next_cup(i: str) -> str:
    i = int(i)
    return str(((i - 2) % 9) + 1)


def main():
    sample = '389125467'
    input = '186524973'
    cups = Cups(input)
    for i in range(100):
        cups.do_move()
    print(cups.cups)
    index_1 = cups.cups.index('1')
    ordered = cups.cups[index_1 + 1:] + cups.cups[:index_1]
    print(f'From 1: {ordered}')
    return ordered


if __name__ == '__main__':
    result = main()
    print(result)