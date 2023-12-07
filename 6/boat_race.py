import re
import pathlib
import math
from functools import reduce
from operator import mul

INPUTS = []

def quadratic_formula(a,b,c, is_lower):
    if is_lower:
        return (-b + math.sqrt(b*b - (4*a*c))) / (2*a)
    else:
        return (-b - math.sqrt(b*b - (4*a*c))) / (2*a)

def solve_roots(input):
    lower =  quadratic_formula(-1, input[0], -input[1], True)
    upper =  quadratic_formula(-1, input[0], -input[1], False)

    return [lower, upper]


def get_times(input):
    roots = solve_roots(input)
    lower = math.ceil(roots[0]) if not roots[0].is_integer() else int(roots[0]) + 1
    upper = math.floor(roots[1]) if not roots[1].is_integer() else int(roots[1]) -1 

    return [lower, upper]

def count_ints(times):
    return len(range(times[0], times[1]+1))

if __name__ == "__main__":
    script_path = str(pathlib.Path(__file__).parent.resolve()) + "/"

    f = open(script_path + "input.txt", "r")
    # f = open(script_path + "test_input.txt", "r")
    a = f.readline()

    times = [ int(x) for x in re.findall("\d+", a) ]
    pt2_time = int("".join(re.findall("\d+", a)))

    a = f.readline()

    distances = [ int(x) for x in re.findall("\d+", a) ]
    pt2_distance = int("".join(re.findall("\d+", a)))

    for i in range(len(times)):
        INPUTS.append([times[i], distances[i]])

    answer1 = []
    for i in INPUTS:
        answer1.append(count_ints(get_times(i)))
    
    print(f"part1: {reduce(mul, answer1)}")

    ### soln 2
    answer2 = count_ints(get_times([pt2_time, pt2_distance]))
    print(f"part2: {answer2}")