import re
from typing import List


class Validator(object):
    def __init__(self, rules):
        self.rules = {}
        self.reduced = {}
        self.rule_regex = re.compile(r'([0-9]+?): (.*)')
        self.unreduced = []
        for rule in rules:
            self.__add_rule(rule)
        self.reduce_rules()

    def __add_rule(self, rule_str: str):
        rule_match = self.rule_regex.match(rule_str)
        num, rule = tuple(rule_match.groups())
        rule = rule.replace('\"', '')
        if rule in ['a', 'b']:
            self.rules[num] = [rule]
            self.reduced[num] = [rule]
        else:
            self.rules[num] = []
            sub_rules = rule.rstrip().split('|')
            for sub in sub_rules:
                self.rules[num].append(tuple(re.findall(r'([0-9]+)', sub)))
            self.unreduced.append(num)

    def reduce_rules(self):
        while len(self.unreduced) > 0:
            for key in self.unreduced:
                if key not in self.reduced.keys():
                    self.reduced[key] = self.resolve_rule(key)

    def resolve_rule(self, key: str) -> List[str]:
        resolved_rule = []
        for t in self.rules[key]:
            inner_rule = ['']
            for r_int in t:
                if r_int not in self.reduced.keys():
                    self.reduced[r_int] = self.resolve_rule(r_int)
                inner_rule = [a + b for a in inner_rule for b in self.reduced[r_int]]
            resolved_rule += inner_rule
        self.unreduced.remove(key)
        return resolved_rule

    def match_rule(self, rule_num: str, test_str: str):
        return test_str in self.reduced[rule_num]


def main():
    with open('inputs/19-rules.txt') as rules_file:
        validator = Validator(rules_file.readlines())
    matches = 0
    with open('inputs/19-input.txt') as input_file:
        for line in input_file:
            if validator.match_rule('0', line.rstrip()):
                matches += 1
    return matches


if __name__ == '__main__':
    result = main()
    print(result)
