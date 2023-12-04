#day3

with open('day3.txt','r') as my_file:
    my_file = my_file.readlines()

lines:list = [element.strip() for element in my_file]

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
numbers = {}
number_coordinates =[]
number=""
for y,line in enumerate(lines):
	for x,letter in enumerate(line):
		if letter.isdigit():
			number+=letter
			number_coordinates.append((x,y))
		elif number != "":
			numbers[int(number)]=number_coordinates
			number_coordinates =[]
			number=""
		if x == len(line)-1 and number != "":
			numbers[int(number)]=number_coordinates
			number_coordinates =[]
			
			
numbers_sum =0
for number, coordinates in numbers.items():
	sum_up = False
	for coordinate in coordinates:
		if coordinate in symbol_coordinates2:
			sum_up = True
	if sum_up:
	#	print(number)
		numbers_sum += number
			
print(numbers.keys())			
print("Part1:",numbers_sum)