import re
from typing import AnyStr, Dict, List, Tuple, Set


# Sample:
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
def process_rule(rule: AnyStr) -> Tuple[AnyStr, List[Tuple[str, str]]]:
    split_rule = rule.split('contain')
    outer_match = re.match('(.*?) bags', split_rule[0])
    outer = outer_match.group(1)
    contained_bags = re.findall('([0-9]+) ([a-z ]+?) bag', split_rule[1])
    return outer, contained_bags


def find_outer_bag_options(bag_color: AnyStr, rules: Dict[str, List[Tuple[str, str]]]) -> Set[AnyStr]:
    outer_bag_colors = set()
    for key, values in rules.items():
        for v in values:
            if v[1] == bag_color:
                outer_bag_colors.add(key)
                outer_bag_colors.update(find_outer_bag_options(key, rules))
    return outer_bag_colors


def count_inner_bags(bag_color: AnyStr, rules: Dict[str, List[Tuple[str, str]]]) -> int:
    count = 0
    inner_bags = rules[bag_color]
    for num, color in inner_bags:
        count += int(num)
        count += int(num) * count_inner_bags(color, rules)
    return count


def main():
    rules = {}
    with open('day7-input.txt') as input_file:
        for line in input_file:
            outer, contains = process_rule(line)
            rules[outer] = contains
    inner_bags = count_inner_bags('shiny gold', rules)
    return inner_bags


if __name__ == '__main__':
    result = main()
    print(result)
