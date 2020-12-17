from typing import Tuple, Set
import sys


# Set is tracking only active spaces
# Top left of input is 0,0,0
class ConwaySpace(object):
    current_active_spaces: Set[Tuple[int, int, int]]

    def __init__(self, starting_layer: [str]):
        self.current_active_spaces = set()
        x = 0
        z = 0
        for line in starting_layer.split():
            for y, c in enumerate(line.rstrip()):
                if c == '#':
                    self.current_active_spaces.add((x, y, z))
            x += 1

    @staticmethod
    def get_space_size(space: Set[Tuple[int, int, int]]) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
        x_max = -sys.maxsize
        x_min = sys.maxsize
        y_max = -sys.maxsize
        y_min = sys.maxsize
        z_max = -sys.maxsize
        z_min = sys.maxsize
        for x, y, z, in space:
            x_max = x_max if x_max > x else x
            x_min = x_min if x_min < x else x
            y_max = y_max if y_max > y else y
            y_min = y_min if y_min < y else y
            z_max = z_max if z_max > z else z
            z_min = z_min if z_min < z else z
        x_range = (x_min - 1, x_max + 1)
        y_range = (y_min - 1, y_max + 1)
        z_range = (z_min - 1, z_max + 1)
        return x_range, y_range, z_range

    def num_active_neighbors(self, x: int, y: int, z: int) -> int:
        num_active = 0
        for x_delta in range(-1, 2):
            for y_delta in range(-1, 2):
                for z_delta in range(-1, 2):
                    if x_delta == y_delta == z_delta == 0:
                        continue
                    if (x + x_delta, y + y_delta, z + z_delta) in self.current_active_spaces:
                        num_active += 1
        return num_active

    def cycle_space(self):
        new_space = set()
        x_range, y_range, z_range = self.get_space_size(self.current_active_spaces)
        for x in range(x_range[0], x_range[1] + 1):
            for y in range(y_range[0], y_range[1] + 1):
                for z in range(z_range[0], z_range[1] + 1):
                    active = (x, y, z) in self.current_active_spaces
                    active_neighbors = self.num_active_neighbors(x, y, z)
                    if active and active_neighbors in [2, 3]:
                        new_space.add((x, y, z))
                    elif not active and active_neighbors == 3:
                        new_space.add((x, y, z))
        self.current_active_spaces = new_space

    def num_active(self):
        return len(self.current_active_spaces)


# Set is tracking only active spaces
# Top left of input is 0,0,0
# noinspection DuplicatedCode
class ConwaySpace4D(object):
    current_active_spaces: Set[Tuple[int, int, int, int]]

    def __init__(self, starting_layer: [str]):
        self.current_active_spaces = set()
        x = 0
        z = 0
        w = 0
        for line in starting_layer.split():
            for y, c in enumerate(line.rstrip()):
                if c == '#':
                    self.current_active_spaces.add((x, y, z, w))
            x += 1

    @staticmethod
    def get_space_size(space: Set[Tuple[int, int, int, int]]) \
            -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
        x_max = -sys.maxsize
        x_min = sys.maxsize
        y_max = -sys.maxsize
        y_min = sys.maxsize
        z_max = -sys.maxsize
        z_min = sys.maxsize
        w_max = -sys.maxsize
        w_min = sys.maxsize
        for x, y, z, w in space:
            x_max = x_max if x_max > x else x
            x_min = x_min if x_min < x else x
            y_max = y_max if y_max > y else y
            y_min = y_min if y_min < y else y
            z_max = z_max if z_max > z else z
            z_min = z_min if z_min < z else z
            w_max = w_max if w_max > w else w
            w_min = w_min if w_min < w else w
        x_range = (x_min - 1, x_max + 1)
        y_range = (y_min - 1, y_max + 1)
        z_range = (z_min - 1, z_max + 1)
        w_range = (w_min - 1, w_max + 1)
        return x_range, y_range, z_range, w_range

    def num_active_neighbors(self, x: int, y: int, z: int, w: int) -> int:
        num_active = 0
        for x_delta in range(-1, 2):
            for y_delta in range(-1, 2):
                for z_delta in range(-1, 2):
                    for w_delta in range(-1, 2):
                        if x_delta == y_delta == z_delta == w_delta == 0:
                            continue
                        if (x + x_delta, y + y_delta, z + z_delta, w + w_delta) in self.current_active_spaces:
                            num_active += 1
        return num_active

    def cycle_space(self):
        new_space = set()
        x_range, y_range, z_range, w_range = self.get_space_size(self.current_active_spaces)
        for x in range(x_range[0], x_range[1] + 1):
            for y in range(y_range[0], y_range[1] + 1):
                for z in range(z_range[0], z_range[1] + 1):
                    for w in range(w_range[0], w_range[1] + 1):
                        active = (x, y, z, w) in self.current_active_spaces
                        active_neighbors = self.num_active_neighbors(x, y, z, w)
                        if active and active_neighbors in [2, 3]:
                            new_space.add((x, y, z, w))
                        elif not active and active_neighbors == 3:
                            new_space.add((x, y, z, w))
        self.current_active_spaces = new_space

    def num_active(self):
        return len(self.current_active_spaces)


def main():
    with open('inputs/17-input.txt') as input_file:
        starting_layer = input_file.read()
    space = ConwaySpace4D(starting_layer)
    for i in range(6):
        space.cycle_space()
    return space.num_active()


if __name__ == '__main__':
    result = main()
    print(result)
