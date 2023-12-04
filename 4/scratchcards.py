import re

# from https://www.geeksforgeeks.org/python-intersection-two-lists/
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

f = open("/home/leviklein/repo/advent_of_code_2023/4/input.txt", "r")
a = f.readline()

sum = 0
row = 1
while a:
    # card = re.search("Card (\d+)", a)
    nums = a.strip().split(':')[1].split('|')
    winning_nums = re.findall("\d+", nums[0])
    have_nums = re.findall("\d+", nums[1])

    matches = len(intersection(winning_nums, have_nums))
    points = 0 if matches <= 0 else pow(2, matches-1)
    sum += points

    a = f.readline()
    row += 1

print(sum)
