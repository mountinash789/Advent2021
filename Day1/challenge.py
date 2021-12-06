def part_one(lst):
    c = 0
    pre = None
    for x in lst:
        x = int(x)
        if pre:
            if x > pre:
                c +=1
    return c

def part_two(lst):
    c = 0
    pre = None
    for i, x in enumerate(lst):
        if i+2 < len(lst):
            summ = sum([int(lst[i]),int(lst[i+1]),int(lst[i+2])])
            if pre:
                if summ > pre:
                   c+=1
    return c
