import re
import pathlib
from itertools import groupby

def print_list(list):
    for line in list:
        print(line)

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def all_zero(iterable):
    return iterable[0] == 0 and all_equal(iterable)

def process_input(a):
    line = [ int(x) for x in re.findall("-*\w+", a) ]
    triangle = [ line ]

    # build triangle
    while True:
        curr_row = triangle[-1]
        next_row = []
        for i in range(1, len(curr_row)):
            next_row.append(curr_row[i] - curr_row[i-1])
        triangle.append(next_row)
        if(all_zero(next_row)):
            break
    #compute answer1
    while True:
        answer1 = 0
        for i in range(-2, -len(triangle)-1, -1):
            if not answer1:
                answer1 = triangle[i][-1]
            else:
                answer1 = triangle[i][-1] + answer1
            triangle[i].append(answer1)
        break
    #compute answer2
    while True:
        answer2 = 0
        for i in range(-2, -len(triangle)-1, -1):
            if not answer2:
                answer2 = triangle[i][0]
            else:
                answer2 = triangle[i][0] - answer2
            triangle[i].insert(0, answer2)
        break
    return answer1, answer2


if __name__ == "__main__":
    script_path = str(pathlib.Path(__file__).parent.resolve()) + "/"

    f = open(script_path + "input.txt", "r")
    # f = open(script_path + "test_input.txt", "r")
    a = f.readline()

    answer1 = 0
    answer2 = 0
    while a:
        res1, res2 = process_input(a.strip())
        answer1 += res1
        answer2 += res2
        a = f.readline()
    print(f"answer1: {answer1}")
    print(f"answer2: {answer2}")