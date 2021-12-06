def part_one(lst):
    c = 0
    pre = None
    for x in lst:
        x = int(x)
        if pre:
            if x > pre:
                c += 1
        pre = x
    return c


def part_two(lst):
    c = 0
    pre = None
    for i, x in enumerate(lst):
        if i + 2 < len(lst):
            sum_ = sum([int(lst[i]), int(lst[i + 1]), int(lst[i + 2])])
            if pre:
                if sum_ > pre:
                    c += 1
            pre = sum_
    return c


if __name__ == "__main__":
    with open('input.txt') as file:
        lst = file.read().split()
        print(part_one(lst))
        print(part_two(lst))
