def part_one(rows):
    open = '([{<'
	close = ')]}>'
	
	count = {}
	
	for row in rows:
		s = []
		for char in row:
			if char in open:
				s.append(char)
			else:
				left = s[-1]
				del s[-1]
				if open.index(left) != close.index(char):
					count[char] = count.get(char, 0) + 1
		
	
	
	ans = sum([count[')'] * 3, count[']'] * 57, count['}'] * 1197, count['>'] * 25137])
	return ans
	
	
def part_two(rows):
    pass


if __name__ == "__main__":
    with open('input.txt') as file:
        lst = file.read().usplit()
        print(part_one(lst))
        print(part_two(lst))
