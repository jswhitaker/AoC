import re
from typing import List, Dict, Tuple, Set
import pprint


class TicketProcessor:
    rules: Dict[str, List[Tuple[int, int]]]
    field_locations: Dict[str, Set[int]]

    def __init__(self):
        self.rules = {}
        self.field_locations = {}

    def add_rule(self, rule: str, field_count: int):
        match = re.match(r'([a-z ]*): ([0-9\-]*) or ([0-9\-]*)', rule)
        name, range1, range2 = match.groups()
        r1_lo, r1_hi = range1.split('-')
        r2_lo, r2_hi = range2.split('-')
        self.rules[name] = [(int(r1_lo), int(r1_hi)), (int(r2_lo), int(r2_hi))]
        self.field_locations[name] = set(range(field_count))

    def check_ticket_invalid(self, ticket: List[int]) -> int:
        invalid_sum = 0
        for field in ticket:
            match = False
            for r1, r2 in self.rules.values():
                if r1[0] <= field <= r1[1] or r2[0] <= field <= r2[1]:
                    match = True
                    break
            if not match:
                invalid_sum += field
        return invalid_sum

    def find_field_locations(self, ticket: List[int]):
        if self.check_ticket_invalid(ticket) == 0:
            for name, ranges in self.rules.items():
                r1, r2 = ranges
                for i, field in enumerate(ticket):
                    if i in self.field_locations[name] and not (r1[0] <= field <= r1[1] or r2[0] <= field <= r2[1]):
                        self.field_locations[name].discard(i)


def main():
    processor = TicketProcessor()
    with open('inputs/16-rules.txt') as input_file:
        rules = input_file.readlines()
    for line in rules:
        processor.add_rule(line.rstrip(), len(rules))

    error_rate = 0
    with open('inputs/16-tickets.txt') as input_file:
        for line in input_file:
            ticket = line.rstrip().split(',')
            ticket = [int(t) for t in ticket]
            # part 1
            error_rate += processor.check_ticket_invalid(ticket)
            # part 2
            processor.find_field_locations(ticket)
    print('Error Rate: ' + str(error_rate))
    print('Field Locations:')
    pprint.pprint(processor.field_locations)


if __name__ == '__main__':
    main()
