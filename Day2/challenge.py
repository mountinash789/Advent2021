def part_one(lst):
    x = y = 0
    for i in lst:
        instruction, amount = i.split()
        if instruction and amount:
            amount = int(amount)
            if instruction == 'forward':
                x += amount
            elif instruction == 'up':
                y -= amount
            elif instruction == 'down':
                y += amount

    return x * y


def part_two(lst):
    x = y = aim = 0
    for i in lst:
        instruction, amount = i.split()
        if instruction and amount:
            amount = int(amount)
            if instruction == 'forward':
                x += amount
                y += amount * aim
            elif instruction == 'up':
                aim -= amount
            elif instruction == 'down':
                aim += amount
    return x * y


if __name__ == "__main__":
    with open('input.txt') as file:
        lst = file.readlines()
        print(part_one(lst))
        print(part_two(lst))
