import re
from typing import Dict, List, Set


def make_dict_unique(dict):
    solved = {}
    while len(solved) < len(dict):
        for k, v in dict.items():
            if k not in solved.keys() and len(v) == 1:
                solved[k] = list(v)[0]
                for vals in dict.values():
                    if len(vals) > 1:
                        vals -= v
    return solved

def main():
    mapping: Dict[str, List[Set[str]]] = {}
    i_lists = []
    with open('inputs/21-input.txt') as input_file:
        for line in input_file:
            ingredients, allergens = tuple(line.split('contains'))
            i_list = re.findall('([a-z]+)', ingredients)
            i_lists.append(i_list)
            a_list = re.findall('([a-z]+)', allergens)
            for a in a_list:
                if a in mapping.keys():
                    mapping[a].append(set(i_list))
                else:
                    mapping[a] = [set(i_list)]
    reduced_mapping = {}
    for k, i in mapping.items():
        reduced_mapping[k] = i[0].intersection(*i[1:])
    solved_mapping = make_dict_unique(reduced_mapping)
    all_i = set()
    for il in i_lists:
        all_i.update(il)
    non_allergens = all_i.difference(set(solved_mapping.values()))
    count = sum([ingreds.count(non_a) for non_a in non_allergens for ingreds in i_lists])
    alpha_allergens = sorted(solved_mapping.keys())
    ordered_ingredients = [solved_mapping[k] for k in alpha_allergens]
    print(','.join(ordered_ingredients))
    return count


if __name__ == '__main__':
    result = main()
    print(result)
