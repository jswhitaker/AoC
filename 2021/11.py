import copy
import itertools
from dataclasses import dataclass
from typing import List


def main():
    rows = []
    with open('inputs/11.txt') as input_file:
        for line in input_file:
            octs = [Octopus(int(c), False) for c in line.strip()]
            rows.append(octs)
    cavern_1 = Cavern(copy.deepcopy(rows))
    cavern_2 = Cavern(copy.deepcopy(rows))
    t1_score = cavern_1.task_1(100)
    t2_score = cavern_2.task_2()
    return t2_score


@dataclass
class Octopus:
    energy: int
    flashed: bool

    def add_energy(self):
        if not self.flashed:
            self.energy += 1

    def should_flash(self):
        return (not self.flashed) and self.energy > 9

    def flash(self):
        self.energy = 0
        self.flashed = True


@dataclass
class Cavern(object):
    grid: List[List[Octopus]]
    max_x: int
    max_y: int

    def __init__(self, grid):
        self.grid = grid
        self.max_y = len(grid) - 1
        self.max_x = len(grid[0]) - 1

    def __str__(self):
        out = ''
        for r in self.grid:
            out += ''.join([str(o.energy) for o in r]) + '\n'
        return out

    def get_neighbors(self, x: int, y: int):
        neighbors = []
        xs = [x-1, x, x+1]
        if x == 0:
            xs.remove(-1)
        elif x == self.max_x:
            xs.remove(self.max_x + 1)
        ys = [y-1, y, y+1]
        if y == 0:
            ys.remove(-1)
        elif y == self.max_y:
            ys.remove(self.max_y + 1)
        cords = itertools.product(xs, ys)
        list_cords = list(cords)
        list_cords.remove((x, y))
        return [self.grid[y][x] for x, y in list_cords]

    def do_step(self):
        # reset flash and increase energy
        for row in self.grid:
            for octopus in row:
                octopus.flashed = False
                octopus.add_energy()
        flash_count = 0
        should_check_flash = True
        while should_check_flash:
            should_check_flash = False
            # print(self)
            for x, y in itertools.product(range(self.max_x + 1), range(self.max_y + 1)):
                octopus = self.grid[y][x]
                if octopus.should_flash():
                    flash_count += 1
                    octopus.flash()
                    neighbors = self.get_neighbors(x, y)
                    for n in neighbors:
                        n.add_energy()
                    should_check_flash = True
        print(self)
        print('Flashes: ' + str(flash_count))
        return flash_count

    def task_1(self, steps: int) -> int:
        count = 0
        print('Before any steps:')
        print(self)
        print('\n')
        for i in range(steps):
            print('Step: ' + str(i + 1))
            count += self.do_step()
            print('Step count: ' + str(count) + '\n\n')
        return count

    def task_2(self):
        step_count = 0
        print('Before any steps:')
        print(self)
        print('\n')
        all_flashed = False
        while not all_flashed:
            step_count += 1
            print('Step: ' + str(step_count))
            self.do_step()
            for x, y in itertools.product(range(self.max_x + 1), range(self.max_y + 1)):
                if not self.grid[y][x].flashed:
                    break
            else:
                return step_count


if __name__ == '__main__':
    result = main()
    print(result)
