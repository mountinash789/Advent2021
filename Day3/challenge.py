import pandas as pd


def occurrence_map(lst, char):
    df = pd.DataFrame(lst)
    out = df.where(df == char, 0).where(df != char, 1)
    return out.mean()


def part_one(lst):
    gamma = []
    epsilon = []

    one = occurrence_map(lst, '1')
    zero = occurrence_map(lst, '0')

    for x in range(12):
        if one[x] > zero[x]:
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')

    return int(''.join(gamma), 2) * int(''.join(epsilon), 2)


def part_two(lst):
    pass


if __name__ == "__main__":
    with open('input.txt') as file:
        data = []
        for line in file.read().split():
            data.append(list(line))
        print(part_one(data))
        # print(part_two(data))
