import re

def overlap(rec1, rec2):
  if (rec2.x2 > rec1.x1 and rec2.x2 < rec1.x2) or \
     (rec2.x1 > rec1.x1 and rec2.x1 < rec1.x2):
    x_match = True
  else:
    x_match = False
  if (rec2.y2 > rec1.y1 and rec2.y2 < rec1.y2) or \
     (rec2.y1 > rec1.y1 and rec2.y1 < rec1.y2):
    y_match = True
  else:
    y_match = False
  if x_match and y_match:
    return True
  else:
    return False
  
def is_overlapping_1D(line1, line2):
    """
    line:
        (xmin, xmax)
    """
    return line1[0] <= line2[1] and line2[0] <= line1[1]

def is_overlapping_2D(box1, box2):
    """
    box:
        (xmin, ymin, xmax, ymax)
    """
    return is_overlapping_1D([box1[0],box1[2]],[box2[0],box2[2]]) and is_overlapping_1D([box1[1],box1[3]],[box2[1],box2[3]])


f = open("/home/leviklein/repo/advent_of_code_2023/3/input.txt", "r")
a = f.readline()
numbers = []
symbols = []
row = 1
while a:
    a = a.strip()
    print(a)
    line_num = re.finditer("(\d+)[^d]?", a) 
    for i in line_num:
        if(len(i.groups())):
            print(i.groups())
            number = i.group(1)
            location = i.span(1)
            num_pair = [number, row, location]
            numbers.append(num_pair)
        
    print(a)
    line_sym = re.finditer("([^\d.])", a) 
    for i in line_sym:
        if(len(i.groups())):
            print(i.groups())
            symbol = i.group(1)
            location = i.span(1)
            sym_pair = [symbol, row, location]
            symbols.append(sym_pair)
        
    a = f.readline()
    row += 1

print(numbers)
print(symbols)

sum = 0

from collections import namedtuple
RECT_NAMEDTUPLE = namedtuple('RECT_NAMEDTUPLE', 'x1 x2 y1 y2')


for number in numbers:
    num = number[0]
    row = number[1]
    loc = number[2]

    candidates = []
    for symbol in symbols:
        sym_row = symbol[1]
        if sym_row >= row-1 and sym_row <= row+1:
            candidates.append(symbol)

    overlap = False
    for candidate in candidates:
        sym_row = candidate[1]
        sym_loc = candidate[2]

        sym_rectangle = RECT_NAMEDTUPLE(sym_loc[0]-1, sym_loc[1], sym_row-1, sym_row+1)

        num_rectangle = RECT_NAMEDTUPLE(loc[0], loc[1]-1, row, row)

        print("sym")
        print(sym_rectangle)
        print("num")
        print(num_rectangle)
        # print ("Overlap found?", overlap(sym_rectangle, sym_rectangle))
        # print (number)
        overlap = is_overlapping_2D((sym_rectangle.x1, sym_rectangle.y1, sym_rectangle.x2, sym_rectangle.y2), (num_rectangle.x1, num_rectangle.y1, num_rectangle.x2, num_rectangle.y2))
        if overlap:
           sum += int(num)
           break
print(sum)