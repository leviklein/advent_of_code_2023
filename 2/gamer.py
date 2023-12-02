import re
from functools import reduce
from operator import mul

def get_color_number(string, color):
    re_pattern = f"(\d+) {color}"
    draw_color = re.search(re_pattern, string) 
    if draw_color is not None:
        return int(draw_color.group(1))
    else:
        return 0

def check_colors_gameover(colors):
    max = [12, 13, 14] # red, green, blue
    for i in range(len(max)):
        if colors[i] > max[i]:
            return True   
    return False

def check_colors_return_max(draw_colors, max_colors):
    for i in range(len(max_colors)):
        if draw_colors[i] > max_colors[i]:
            max_colors[i] = draw_colors[i]
    return max_colors

f = open("/home/leviklein/repo/advent_of_code_2023/2/input.txt", "r")
a = f.readline()

total_powers = 0
total_games = 0
while a:
    game = re.search("Game (\d+):", a)
    idx = game.end()
    game = int(game.group(1))

    draws = a[idx:].split(';')
    print(draws)

    game_over = False
    max_colors = [1, 1, 1]

    for draw in draws:
        draw_red = get_color_number(draw, "red")
        draw_green = get_color_number(draw, "green")
        draw_blue = get_color_number(draw, "blue")
        draw_colors = [draw_red, draw_green, draw_blue]

        max_colors = check_colors_return_max(draw_colors, max_colors)
        if check_colors_gameover(draw_colors):
            game_over = True

    if not game_over:
        total_games += game

    power = reduce((lambda x, y: x * y), max_colors)
    power = reduce(mul, max_colors)
    total_powers += power

    a = f.readline()

print(total_games)
print(total_powers)