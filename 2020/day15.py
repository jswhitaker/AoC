def main():
    # print(brute_force(2020))
    return cached_solution(30000000)


# Part 1 solution
def brute_force(number_spoken: int) -> int:
    # most recently spoken is index 0, first spoken is at the end.
    spoken = [0, 7, 4, 1, 5, 15]

    for i in range(number_spoken - len(spoken)):
        if spoken[0] not in spoken[1:]:
            spoken.insert(0, 0)
        else:
            spoken.insert(0, spoken.index(spoken[0], 1))
    return spoken[0]


def cached_solution(number_spoken: int) -> int:
    spoken = {15: 0,
              5: 1,
              1: 2,
              4: 3,
              7: 4}
    last_age = 0
    for i in range(5, number_spoken - 1):
        age = i - spoken.get(last_age, i)
        spoken[last_age] = i
        last_age = age
    return last_age


if __name__ == '__main__':
    result = main()
    print(result)
