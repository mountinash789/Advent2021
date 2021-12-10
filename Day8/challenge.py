def part_one(rows):
    low_points = []



    for row_i, row in enumerate(rows):
	    first_row = False
	    last_row = False
	    up_higher = False
	    down_higher = False
	
	    if row_i == 0:
	        first_row = True
		    up_higher =True
	
	    if row_i + 1 == len(rows):
		
		    last_row = True
		    down_higher = True
	
	    for v_i, v in enumerate(row):
		    v = int(v)
	
		    first_col = False
		    last_col = False
		
		    l_higher = False
		    r_higher = False
		
		    if v_i == 0:
			    first_col = True
			    l_higher =True
	
		    if v_i + 1 == len(row):
			    last_col = True
			    r_higher = True
			
		    if not first_row:
		        if v < int(rows[row_i-1][v_i]):
		   		    up_higher = True
		        else:
			        up_higher = False
		   
		    if not last_row:
		        if v < int(rows[row_i+1][v_i]):
		   		    down_higher = True
		        else:
			        down_higher = False
			
		
		    if not first_col:
		        if v < int(rows[row_i][v_i-1]):
		            l_higher = True
		        else:
			        l_higher =False
			
				
		    if not last_col:
		        if v < int(rows[row_i][v_i+1]):
		            r_higher = True
		        else:
			        r_higher =False
			
		
	
		    if all([up_higher, down_higher, l_higher, r_higher]):
			    low_points.append(v)
	

    return sum([x+1 for x in low_points])


def part_two():
    pass


if __name__ == "__main__":
    with open('input.txt') as file:
        lst = file.read().split()
        print(part_one(lst))
        print(part_two(lst))

