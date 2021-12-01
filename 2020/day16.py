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

    def check_ticket_invalid(self, ticket: List[int]) -> Tuple[bool, int]:
        invalid_sum = 0
        valid_match = True
        for field in ticket:
            match = False
            for r1, r2 in self.rules.values():
                if r1[0] <= field <= r1[1] or r2[0] <= field <= r2[1]:
                    match = True
                    break
            if not match:
                invalid_sum += field
                valid_match = False
        return valid_match, invalid_sum

    def find_field_locations(self, ticket: List[int]):
        # Discard invalid tickets
        valid, _ = self.check_ticket_invalid(ticket)
        if not valid:
            return

        # Remove potential field location if ticket's field does not pass the rules.
        for name, (r1, r2) in self.rules.items():
            for i, field in enumerate(ticket):
                if i in self.field_locations[name] and not (r1[0] <= field <= r1[1] or r2[0] <= field <= r2[1]):
                    self.field_locations[name].discard(i)

    def solve_field_locations(self):
        solved = []
        while len(solved) < len(self.field_locations):
            curr_location = set()
            for field, locs in self.field_locations.items():
                if field not in solved and len(locs) == 1:
                    curr_location = locs
                    solved.append(field)
            for locs in self.field_locations.values():
                if len(locs) > 1:
                    locs -= curr_location

    # only call after solving field locations!!
    def departure_mul(self, ticket: List[int]) -> int:
        result = 1
        for field, index in self.field_locations.items():
            if field.startswith('departure'):
                result *= ticket[list(index)[0]]
        return result


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
            _, rate = processor.check_ticket_invalid(ticket)
            error_rate += rate
            # part 2
            processor.find_field_locations(ticket)
    processor.solve_field_locations()
    print('Error Rate: ' + str(error_rate))
    print('Field Locations:')
    pprint.pprint(processor.field_locations)
    dep_mul = processor.departure_mul(
        [127, 89, 149, 113, 181, 131, 53, 199, 103, 107, 97, 179, 109, 193, 151, 83, 197, 101, 211, 191])
    print('Part 2: ' + str(dep_mul))


if __name__ == '__main__':
    main()
