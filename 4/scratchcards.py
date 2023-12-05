import re
from functools import reduce
from operator import add

# from https://www.geeksforgeeks.org/python-intersection-two-lists/
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

f = open("/home/leviklein/repo/advent_of_code_2023/4/test_input.txt", "r")
f = open("/home/leviklein/repo/advent_of_code_2023/4/input.txt", "r")
a = f.readline()

sum = 0
row = 1
scratchcards = {1: 0}
while a:
    scratchcards.update({row: scratchcards.get(row, 0) + 1})
    multiplier = scratchcards.get(row)
    nums = a.strip().split(':')[1].split('|')
    winning_nums = re.findall("\d+", nums[0])
    have_nums = re.findall("\d+", nums[1])

    matches = len(intersection(winning_nums, have_nums))
    points = 0 if matches <= 0 else pow(2, matches-1)
    sum += points
    for i in range(matches):
        new_count = scratchcards.get(row+i+1, 0) + multiplier
        new_row = row+i+1
        scratchcards.update({new_row: new_count})
        # scratchcards[row+i] += 1

    a = f.readline()
    row += 1
print(f"points: {sum}")
print(f"scratchcards: {reduce(add, scratchcards.values())}")
