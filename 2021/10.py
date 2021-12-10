import statistics
from typing import List, Optional


def main():
    rows = []
    with open('inputs/10.txt') as input_file:
        for line in input_file:
            pbs = [c for c in line.strip()]
            rows.append(pbs)
    t1_score = task_1(rows)
    return t1_score, task_2(rows)


def task_1(rows: List[List[str]]) -> List[str]:
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    bad_chars = []
    for r in rows:
        bc = find_corrupted(r)
        if bc is not None:
            bad_chars.append(bc)
    return sum([points[b] for b in bad_chars])


def task_2(rows):
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    rev_pairs = {y: x for x, y in pairs.items()}
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for r in rows:
        if find_corrupted(r) is not None:
            continue
        remainder = find_incomplete(r)
        score = 0
        for c in remainder[::-1]:
            score = score * 5
            score += points[pairs[c]]
        scores.append(score)
    return statistics.median(scores)


def find_corrupted(row: List[str]) -> Optional[str]:
    temp_row = []
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    rev_pairs = {y: x for x, y in pairs.items()}
    for c in row:
        if c in ['(', '[', '{', '<']:
            temp_row.append(c)
        else:
            if not temp_row.pop() == rev_pairs[c]:
                return c
    return None


def find_incomplete(row: List[str]) -> List[str]:
    temp_row = []
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    rev_pairs = {y: x for x, y in pairs.items()}
    for c in row:
        if c in ['(', '[', '{', '<']:
            temp_row.append(c)
        else:
            if not temp_row.pop() == rev_pairs[c]:
                raise Exception
    return temp_row


if __name__ == '__main__':
    result = main()
    print(result)
