#day2.py

with open('day2.txt','r') as my_file:
    my_file = my_file.readlines()

lines:list = [element.strip() for element in my_file]

games_dict ={}
for line in lines:
	gaming_list = line.split(":")
	#create id
	gaming_list[0] = int(gaming_list[0].replace("Game ","").strip())
	#create game tuples
	games = gaming_list[1].replace(";",",").split(",")
	games = [tuple(game.strip().split(" ")) for game in games]
	games_dict[gaming_list[0]]=games
	
###PART1
sum_id =0
for id, games in games_dict.items():
	for game in games:
		if "red" in game and int(game[0]) > 12:
			id = 0
		if "blue" in game and int(game[0]) > 14:
			id = 0
		if "green" in game and int(game[0]) > 13:
			id = 0
	sum_id += id

print("Part1:",sum_id)
sum_power = 0
###PART2
for id, games in games_dict.items():
	r,b,g =0,0,0 
	for game in games:
		if "red" in game and int(game[0]) > r:
			r = int(game[0])
		if "blue" in game and int(game[0]) > b:
			b = int(game[0])
		if "green" in game and int(game[0]) > g:
			g = int(game[0])
	power = r * b * g
	sum_power += power
	
print("Part2:",sum_power)