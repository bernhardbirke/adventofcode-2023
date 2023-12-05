#day3

with open('day3.txt','r') as my_file:
    my_file = my_file.readlines()

lines:list = [element.strip() for element in my_file]

###PART1
"""
symbol_list = []
[symbol_list.extend(list(line)) for line in lines]
symbols = list(set(symbol_list))
symbols.remove(".")
for i in range(10):
	symbols.remove(str(i))

symbol_coordinates = []
for y,line in enumerate(lines):
	for x,letter in enumerate(line):
		if letter in symbols:
			symbol_coordinates.append((x,y))


#coordinates around each symbol
symbol_coordinates2 =[]
for co_x, co_y in symbol_coordinates:
	symbol_coordinates2.extend([(co_x-1,co_y-1),(co_x-1,co_y),(co_x-1,co_y+1),(co_x,co_y-1),(co_x,co_y),(co_x,co_y+1),(co_x+1,co_y-1),(co_x+1,co_y),(co_x+1,co_y+1)])
	
#numbers and corresponding coordinates
numbers = []
for y,line in enumerate(lines):
	number_coordinates =[]
	number=""
	for x,letter in enumerate(line):
		if letter.isdigit():
			number+=letter
			number_coordinates.append((x,y))
		elif number != "":
			numbers.append([int(number),number_coordinates])
			number_coordinates =[]
			number=""
		if x == len(line)-1 and number != "":
			numbers.append([int(number),number_coordinates])
			
numbers_sum =0
for number, coordinates in numbers:
	sum_up = False
	for coordinate in coordinates:
		if coordinate in symbol_coordinates2:
			sum_up = True
	if sum_up:
		numbers_sum += number

print("Part1:",numbers_sum)
"""

symbol_coordinates = []
for y,line in enumerate(lines):
	for x,letter in enumerate(line):
		if letter == "*":
			symbol_coordinates.append((x,y))
			
#coordinates around each symbol
symbol_dict = {}
for co_x, co_y in symbol_coordinates:
	symbol_coordinates2 =[]
	symbol_coordinates2.extend([(co_x-1,co_y-1),(co_x-1,co_y),(co_x-1,co_y+1),(co_x,co_y-1),(co_x,co_y+1),(co_x+1,co_y-1),(co_x+1,co_y),(co_x+1,co_y+1)])
	symbol_dict[(co_x,co_y)] = symbol_coordinates2


#numbers and corresponding coordinates
numbers = []
for y,line in enumerate(lines):
	number_coordinates =[]
	number=""
	for x,letter in enumerate(line):
		if letter.isdigit():
			number+=letter
			number_coordinates.append((x,y))
		elif number != "":
			numbers.append([int(number),number_coordinates])
			number_coordinates =[]
			number=""
		if x == len(line)-1 and number != "":
			numbers.append([int(number),number_coordinates])

gear_sum = 0
for symbol, symbol_coordinates in symbol_dict.items():
	all_numbers =[]
	for number, number_coordinates in numbers:
		if any(i in symbol_coordinates for i in number_coordinates):
			all_numbers.append(number)
	if len(all_numbers) == 2:
		gear_sum += all_numbers[0] * all_numbers[1]


print("Part2: ", gear_sum)