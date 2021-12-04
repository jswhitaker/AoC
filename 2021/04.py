import itertools

def main():
    groups = []
    with open('inputs/04.txt') as input_file:
        data = input_file.read()
        groups = data.split('\n\n')
    called = groups[0].split(',')
    cards = [[line.split() for line in c.split('\n')] for c in groups[1:]]
    rotated = [list(zip(*c)) for c in cards]
    scores = []

    curr_called = called[:4]

    card_idxs = list(range(len(cards)))

    for num in called[4:]:
        curr_called.append(num)
        for i in card_idxs:
            c = cards[i]
            r = rotated[i]
            score = test_card(c, r, curr_called)
            if score is not None:
                scores.append((i, len(curr_called), score))
                card_idxs.remove(i)
    return scores


def test_card(card, rotated, curr_called):
    for c_line in card:
        c_found = True
        for c_num in c_line:
            c_found = c_found and (c_num in curr_called)
            if not c_found:
                break
        if c_found:
            score = calc_score(card, curr_called)
            return score
    for r_line in rotated:
        r_found = True
        for r_num in r_line:
            r_found = r_found and (r_num in curr_called)
            if not r_found:
                break
        if r_found:
            score = calc_score(rotated, curr_called)
            return score
    return None


def calc_score(card, curr_called):
    card_nums = list(itertools.chain(*card))
    unmatched_nums = [int(num) for num in card_nums if num not in curr_called]
    score = sum(unmatched_nums) * int(curr_called[len(curr_called)-1])
    return score


if __name__ == '__main__':
    result = main()
    print(result)
