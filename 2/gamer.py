import re

f = open("/home/leviklein/repo/advent_of_code_2023/2/input.txt", "r")
a = f.readline()

max_red = 12
max_green = 13
max_blue = 14


total = 0
while a:
    game = re.search("Game (\d+):", a)
    idx = game.end()
    game = int(game.group(1))

    draws = a[idx:].split(';')
    print(draws)

    game_over = False
    for draw in draws:
        if re.search("(\d+) red", draw) is not None:
            if int(re.search("(\d+) red", draw).group(1)) > max_red: 
                game_over = True
                break
        if re.search("(\d+) green", draw) is not None:
            if int(re.search("(\d+) green", draw).group(1)) > max_green: 
                game_over = True
                break
        if re.search("(\d+) blue", draw) is not None:
            if int(re.search("(\d+) blue", draw).group(1)) > max_blue: 
                game_over = True
                break

    if not game_over:
        total += game

    a = f.readline()

print(total)