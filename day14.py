import re


class ProgramConverter(object):
    def __init__(self):
        self.mem = {}
        self.mask = ''
        self.one_mask = ''
        self.zero_mask = ''

    def process_mask(self, mask: str):
        self.mask = mask
        self.one_mask = mask.replace('X', '0')  # Use with OR
        self.zero_mask = mask.replace('X', '1')  # Use with AND

    def update_memory(self, loc: int, value: int):
        value = value | int(self.one_mask, 2)
        value = value & int(self.zero_mask, 2)
        self.mem[loc] = value

    def parse_input_line(self, line: str):
        match = re.match(r'(mem|mask)\[?([0-9]*?)]? = ([X0-9].*)', line)
        groups = match.groups()
        if groups[0] == 'mask':
            self.process_mask(groups[2])
        else:
            self.update_memory(int(groups[1]), int(groups[2]))


def main():
    program_converter = ProgramConverter()
    with open('inputs/14-input.txt') as input_file:
        for line in input_file:
            program_converter.parse_input_line(line)
    return sum(program_converter.mem.values())


if __name__ == '__main__':
    result = main()
    print(result)
