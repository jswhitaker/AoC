#  N
# W  E
#  S
# ship starts facing E
# East and North are positive
# South and West are negative
# Ship starts at at 0,0 for both parts


class Ship(object):
    def __init__(self):
        self.ns = 0
        self.ew = 0
        self.current_direction = 1
        self.directions = ['N', 'E', 'S', 'W']
        self.waypoint = Waypoint()

    # part1
    def execute_instruction(self, instruction, instruction_num):
        if instruction == 'F':
            self.execute_instruction(self.directions[self.current_direction], instruction_num)
        elif instruction == 'R':
            direction_delta = instruction_num / 90
            self.current_direction = int(self.current_direction + direction_delta) % 4
        elif instruction == 'L':
            direction_delta = instruction_num / 90
            self.current_direction = int(self.current_direction - direction_delta) % 4
        elif instruction == 'N':
            self.ns += instruction_num
        elif instruction == 'S':
            self.ns -= instruction_num
        elif instruction == 'E':
            self.ew += instruction_num
        elif instruction == 'W':
            self.ew -= instruction_num

    # part2, only F actually moves the ship. All other commands go to the waypoint.
    def move_ship(self, instruction, instruction_num):
        if instruction == 'F':
            self.ns += self.waypoint.ns * instruction_num
            self.ew += self.waypoint.ew * instruction_num
        else:
            self.waypoint.update_waypoint(instruction, instruction_num)

    def get_distance(self):
        return abs(self.ns) + abs(self.ew)


# Waypoint starts at 1 N/S and 10 E/W
class Waypoint(object):
    def __init__(self):
        self.ns = 1
        self.ew = 10

    def update_waypoint(self, instruction, instruction_num):
        if instruction == 'R':
            direction_delta = int(instruction_num / 90)
            for i in range(direction_delta):
                old_ns = self.ns
                old_ew = self.ew
                self.ew = old_ns
                self.ns = old_ew * -1
        elif instruction == 'L':
            direction_delta = int(instruction_num / 90)
            for i in range(direction_delta):
                old_ns = self.ns
                old_ew = self.ew
                self.ew = old_ns * -1
                self.ns = old_ew
        elif instruction == 'N':
            self.ns += instruction_num
        elif instruction == 'S':
            self.ns -= instruction_num
        elif instruction == 'E':
            self.ew += instruction_num
        elif instruction == 'W':
            self.ew -= instruction_num


def main():
    ship = Ship()
    with open('inputs/12-input.txt') as input_file:
        for line in input_file:
            instruction = line[0]
            instruction_num = int(line[1:])
            ship.move_ship(instruction, instruction_num)
    return ship.get_distance()


if __name__ == '__main__':
    result = main()
    print(result)
