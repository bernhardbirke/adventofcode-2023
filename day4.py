#day4.py

with open('day4.txt','r') as my_file:
    my_file = my_file.readlines()

lines:list = [element.strip() for element in my_file]

"""
###PART1
#make lists with winning numbers and have numbers
points = 0
for line in lines:
	line_list = (line.split(":")[1].split("|"))
	winning_no = line_list[0].strip().replace("  "," ").split(" ")
	have_no = line_list[1].strip().replace("  "," ").split(" ")
	power = 0
	for number in have_no:
		if number in winning_no:
			power+=1
	if power > 0:
		points += 2**(power-1)

print("Part1:", points)
"""

###PART2
## dict with id and count of each card
line_numbers = dict(zip(range(len(lines)), [1]*len(lines)))


for no, line in enumerate(lines):
	n = line_numbers[no]
	#use the card n times 
	while n>0:
		line_list = (line.split(":")[1].split("|"))
		winning_no = line_list[0].strip().replace("  "," ").split(" ")
		have_no = line_list[1].strip().replace("  "," ").split(" ")
		power = 0
		for number in have_no:
			if number in winning_no:
				power+=1
		#power -> sum of winning numbers of line
		#gain cards according to power
		while power > 0:
			line_numbers[no+power] += 1
			power -=1
				
		n-=1

print("Part2:", sum(line_numbers.values()))


