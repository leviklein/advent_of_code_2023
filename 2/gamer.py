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
    game_max_red = 1
    game_max_green = 1
    game_max_blue = 1

    # for draw in draws:
    #     if re.search("(\d+) red", draw) is not None:
    #         if int(re.search("(\d+) red", draw).group(1)) > max_red: 
    #             game_over = True
    #             break
    #     if re.search("(\d+) green", draw) is not None:
    #         if int(re.search("(\d+) green", draw).group(1)) > max_green: 
    #             game_over = True
    #             break
    #     if re.search("(\d+) blue", draw) is not None:
    #         if int(re.search("(\d+) blue", draw).group(1)) > max_blue: 
    #             game_over = True
    #             break

    ## problem 2
    for draw in draws:
        draw_red = re.search("(\d+) red", draw) 
        if draw_red is not None:
            draw_red = int(draw_red.group(1))
            if draw_red > game_max_red: 
                game_max_red = draw_red
        draw_green = re.search("(\d+) green", draw) 
        if draw_green is not None:
            draw_green = int(draw_green.group(1))
            if draw_green > game_max_green: 
                game_max_green = draw_green
        draw_blue = re.search("(\d+) blue", draw) 
        if draw_blue is not None:
            draw_blue = int(draw_blue.group(1))
            if draw_blue > game_max_blue: 
                game_max_blue = draw_blue


    # if not game_over:
    #     total += game
    power = game_max_red * game_max_green * game_max_blue
    total += power

    a = f.readline()

print(total)