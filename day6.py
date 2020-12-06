import string

def main():
    foo = string.ascii_lowercase
    data = ''
    with open('day6-input.txt') as input_file:
        data = input_file.read()
    groups = data.split('\n\n')
    group_yeses = []
    for g in groups:
        group_yeses.append(any_yes(g))
    return group_yeses

def all_yes(group):
    yes_set = set(list(string.ascii_lowercase))
    temp_set = set()
    people = group.split()
    for p in people:
        temp_set.clear()
        for char in p.strip:
            temp_set.add(char)
        yes_set = yes_set.intersection(temp_set)
    return yes_set

def any_yes(group):
    people = group.split()
    question_set = set()
    for p in people:
        for char in p.strip():
            question_set.add(char)
    return question_set


if __name__ == '__main__':
    result = main()
    yes_sum = 0
    for r in result:
        yes_sum += len(r)
    print(yes_sum)
