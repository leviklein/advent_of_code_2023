import re

f = open("/home/leviklein/repo/advent_of_code_2023/1/input.txt", "r")
a = f.readline()
total = 0

while a:
    print(a)
    a = a.replace("one", "o1e")
    a = a.replace("two", "t2o")
    a = a.replace("three", "t3e")
    a = a.replace("four", "f4r")
    a = a.replace("five", "f5e")
    a = a.replace("six", "s6x")
    a = a.replace("seven", "s7n")
    a = a.replace("eight", "e8t")
    a = a.replace("nine", "n9e")
    a = a.replace("ten", "z0o")

    print(a)

    x = re.findall("\d", a)
    # print(x)
    tens = int(x[0]) * 10
    ones = int(x[-1])
    num = tens + ones
    # print(num)
    
    total += num

    a = f.readline()

print(total)
