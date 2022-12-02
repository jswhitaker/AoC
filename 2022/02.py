choices = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}
outcomes = {'X':0, 'Y':3, 'Z':6}
def main():
    with open('inputs/02.txt') as input_file:
        total_score = 0
        for line in input_file:
            score = 0
            opp, you = line.strip().split(' ')
            score += choices[you]
            if choices[you] == (choices[opp] % 3) + 1:
                score += 6
            elif choices[you] == choices[opp]:
                score += 3
            total_score += score
        return total_score


def main_2():
    with open('inputs/02.txt') as input_file:
        total_score = 0
        for line in input_file:
            score = 0
            opp, outcome = line.strip().split(' ')
            score += outcomes[outcome]
            if outcome == 'X':
                score += ((choices[opp] - 2) % 3) + 1
            elif outcome == 'Y':
                score += choices[opp]
            else:
                score += (choices[opp] % 3) + 1
            total_score += score
        return total_score

def round_score(opp:str, you:str) -> int :
    score = choices[you]
    if choices[you] == (choices[opp] + 1) % 3:
        score += 6
    elif choices[you] == choices[opp]:
        score += 3
    return score

if __name__ == '__main__':
    result = main()
    print(result)
    result = main_2()
    print(result)
