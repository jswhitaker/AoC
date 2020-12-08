def process_instruction(operation, accumulator, instructions):
    acc = accumulator
    next_op = operation
    if instructions[operation][0] == 'acc':
        next_op = operation + 1
        acc += instructions[operation][1]
    elif instructions[operation][0] == 'jmp':
        next_op = operation + instructions[operation][1]
    elif instructions[operation][0] == 'nop':
        next_op = operation + 1
    return next_op, acc


def main():
    instructions = []
    with open('day8-input.txt') as input_file:
        for line in input_file:
            line_split = line.rstrip().split()
            instructions.append((line_split[0], int(line_split[1])))
    hit_loop = False
    op = 0
    acc = 0
    visited = []
    while not hit_loop:
        next_op, acc = process_instruction(op, acc, instructions)
        visited.append(op)
        op = next_op
        if next_op in visited:
            hit_loop = True
    return acc


if __name__ == '__main__':
    result = main()
    print(result)
