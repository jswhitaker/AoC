def main() -> str:
    with open('inputs/05.txt') as input_file:
        diagram, instructions = input_file.read().split('\n\n')
        diagram_2 = diagram.split('\n')
        stacks = [''.join(c)[::-1] for c in zip(*diagram_2)]
        stacks_dict = {}
        for s in stacks:
            if s[0].isnumeric():
                stacks_dict[int(s[0])] = list(s.rstrip()[1:])
        for i in instructions.split('\n'):
            parts = i.rstrip().split(' ')
            for boxes in range(int(parts[1])):
                box = stacks_dict[int(parts[3])].pop()
                stacks_dict[int(parts[5])].append(box)
        columns = list(stacks_dict.keys())
        columns.sort()
        tops = []
        for c in columns:
            tops.append(stacks_dict[c][-1])
        return ''.join(tops)


def main_2() -> str:
    with open('inputs/05.txt') as input_file:
        diagram, instructions = input_file.read().split('\n\n')
        diagram_2 = diagram.split('\n')
        stacks = [''.join(c)[::-1] for c in zip(*diagram_2)]
        stacks_dict = {}
        for s in stacks:
            if s[0].isnumeric():
                stacks_dict[int(s[0])] = list(s.rstrip()[1:])
        for i in instructions.split('\n'):
            _, box_count, _, from_col, _, to_col = i.rstrip().split(' ')
            box_count = int(box_count)
            from_col = int(from_col)
            to_col = int(to_col)
            boxes = stacks_dict[from_col][len(stacks_dict[from_col]) - box_count:]
            del stacks_dict[from_col][len(stacks_dict[from_col]) - int(box_count):]
            stacks_dict[to_col].extend(boxes)
        columns = list(stacks_dict.keys())
        columns.sort()
        tops = []
        for c in columns:
            tops.append(stacks_dict[c][-1])
        return ''.join(tops)


if __name__ == '__main__':
    result = main()
    print(result)
    result = main_2()
    print(result)
