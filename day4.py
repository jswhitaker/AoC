import re

def validator(key, value):
    if key == 'byr':
        return 1920 <= int(value) <= 2002
    elif key == 'iyr':
        return 2010 <= int(value) <= 2020
    elif key == 'eyr':
        return 2020 <= int(value) <= 2030
    elif key == 'hgt':
        if value.find('cm') > 0:
            hgt = value.removesuffix('cm')
            return 150 <= int(hgt) <= 193
        elif value.find('in') > 0:
            hgt = value.removesuffix('in')
            return 59 <= int(hgt) <= 76
    elif key == 'hcl':
        return re.fullmatch('#[0-9a-f]{6}', value) is not None
    elif key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':
        return re.fullmatch('[0-9]{9}', value)
    else:
        return False


def main(required):
    count = 0
    fields = {}
    with open('day4-input.txt') as input_file:
        for line in input_file:
            if line == '\n':
                i = 0
                for k, v in fields.items():
                    if validator(k, v):
                        i += 1
                if i == len(required):
                    count += 1
                fields = {}
            else:
                pairs = line.strip().split()
                for p in pairs:
                    key_val = p.split(':')
                    fields[key_val[0]] = key_val[1]
    return count


if __name__ == '__main__':
    result = main(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    print(result)
