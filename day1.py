#day1.py

with open('day1.txt','r') as my_file:
    my_file = my_file.readlines()

lines:list = [element.strip() for element in my_file]

### PART 1
"""
numberslist: list[int] = []
for line in lines:
	numbers_line = [letter for letter in line if letter.isnumeric()]
	number = int(str(numbers_line[0])+str(numbers_line[-1]))
	numberslist.append(number)

print(sum(numberslist))
"""

### PART 2

replacement_list: list[tuple] = list(zip(["one","two","three","four","five","six","seven","eight","nine"],["o1e","t2o","t3e","f4r","f5e","s6x","s7n","e8t","n9n"]))

numberslist: list[int] = []
for line in lines:
	k = 0
	for k in range(len(line)+1):
		subline = line[:k]
		for i,j in replacement_list:
			subline = subline.replace(i,str(j))
		line = subline + line[k:]
		k+=1
	numbers_line = [letter for letter in line if letter.isnumeric()]
	number = int(str(numbers_line[0])+str(numbers_line[-1]))
	numberslist.append(number)

print("number of lines: ", len(numberslist))
print(sum(numberslist))



