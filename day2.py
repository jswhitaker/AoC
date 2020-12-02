from collections import namedtuple
from typing import List, Any

PasswordEntry = namedtuple('PasswordEntry', ['low', 'high', 'letter', 'password'])

# moved from main for part 2
def part1():
    password_entries: List[PasswordEntry] = []
    with open('day2-input.txt') as password_file:
        for line in password_file:
            low, _, remainder = line.partition('-')
            high, _, remainder = remainder.partition(' ')
            letter, _, password = remainder.partition(': ')
            password_entries.append(PasswordEntry(int(low), int(high), letter, password))

    correct_count = 0
    for entry in password_entries:
        count = entry.password.count(entry.letter)
        if entry.low <= count <= entry.high:
            correct_count = correct_count + 1
    return correct_count

def main():
    password_entries: List[PasswordEntry] = []
    with open('day2-input.txt') as password_file:
        for line in password_file:
            low, _, remainder = line.partition('-')
            high, _, remainder = remainder.partition(' ')
            letter, _, password = remainder.partition(': ')
            password_entries.append(PasswordEntry(int(low), int(high), letter, password))

    correct_count = 0
    for entry in password_entries:
        count = entry.password.count(entry.letter)
        if entry.low <= count <= entry.high:
            correct_count = correct_count + 1
    return correct_count


if __name__ == '__main__':
    print(main())
