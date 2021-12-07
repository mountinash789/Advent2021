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

    for x in range(len(lst[0])):
        if one[x] > zero[x]:
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')

    return int(''.join(gamma), 2) * int(''.join(epsilon), 2)


def myfilter(lst, char, pos, match):
    if len(lst) == 1:
        return lst.pop()

    one = occurrence_map(lst, '1')
    zero = occurrence_map(lst, '0')
    if one[pos] > zero[pos]:
        if char == '1':
            match.append('1')
        else:
            match.append('0')
    elif one[pos] < zero[pos]:
        if char == '1':
            match.append('0')
        else:
            match.append('1')
    else:
        match.append(char)
    lst = list(filter(lambda x: x[:pos + 1] == match, lst))

    return myfilter(lst, char, pos + 1, match)


def part_two(lst):
    oxygen = myfilter(lst, '1', 0, [])
    co2 = myfilter(lst, '0', 0, [])
    return int(''.join(oxygen), 2) * int(''.join(co2), 2)


if __name__ == "__main__":
    with open('input.txt') as file:
        data = []
        for line in file.read().split():
            data.append(list(line))
        print(part_one(data))
        print(part_two(data))
