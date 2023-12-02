import re

def get_color_number(string, color):
    re_pattern = f"(\d+) {color}"
    draw_color = re.search(re_pattern, string) 
    if draw_color is not None:
        return int(draw_color.group(1))
    else:
        return 0



f = open("/home/leviklein/repo/advent_of_code_2023/2/input.txt", "r")
a = f.readline()

max_red = 12
max_green = 13
max_blue = 14


total_powers = 0
total_games = 0
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
    #     draw_red = get_color_number(draw, "red")
    #     if draw_red > max_red: 
    #         game_over = True
    #     draw_green = get_color_number(draw, "green")
    #     if draw_green > max_green: 
    #         game_over = True
    #     draw_blue = get_color_number(draw, "blue")
    #     if draw_blue > max_blue: 
    #         game_over = True


    ## problem 2
    for draw in draws:
        draw_red = get_color_number(draw, "red")
        if draw_red > game_max_red: 
            game_max_red = draw_red
        if draw_red > max_red: 
            game_over = True

        draw_green = get_color_number(draw, "green")
        if draw_green > game_max_green: 
            game_max_green = draw_green
        if draw_green > max_green: 
            game_over = True

        draw_blue = get_color_number(draw, "blue")
        if draw_blue > game_max_blue: 
            game_max_blue = draw_blue
        if draw_blue > max_blue: 
            game_over = True


    if not game_over:
        total_games += game

    power = game_max_red * game_max_green * game_max_blue
    total_powers += power

    a = f.readline()

print(total_games)
print(total_powers)