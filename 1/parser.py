import re

f = open("/home/leviklein/repo/advent_of_code_2023/1/input.txt", "r")
a = f.readline()
total = 0
count = 1
w = open("/home/leviklein/repo/advent_of_code_2023/1/output.txt", "w")
while a:
    # print(a)
    ##### correct solution
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
    ##### end

    print(a)

    x = re.findall("\d", a)

    ##### experimental solution
    # x = re.findall("\d|one|two|three|four|five|six|seven|eight|nine|zero", a)
    # print(x)
    # for j in range(len(x)):
    #     x[j] = x[j].replace("one", "1")
    #     x[j] = x[j].replace("two", "2")
    #     x[j] = x[j].replace("three", "3")
    #     x[j] = x[j].replace("four", "4")
    #     x[j] = x[j].replace("five", "5")
    #     x[j] = x[j].replace("six", "6")
    #     x[j] = x[j].replace("seven", "7")
    #     x[j] = x[j].replace("eight", "8")
    #     x[j] = x[j].replace("nine", "9")
    #     x[j] = x[j].replace("ten", "0")
    ##### end 

    tens = int(x[0]) * 10
    ones = int(x[-1])
    num = tens + ones
    # print(count)
    print(f"{count}: {num}", file=w)
    print(x, file=w)
    # print(num)
    
    total += num
    count += 1
    a = f.readline()

print(total) #54581
