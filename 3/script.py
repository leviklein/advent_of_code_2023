import re
from functools import reduce
from operator import mul

def is_overlapping_RECT_TUPLE(rect1, rect2):
    return is_overlapping_2D((rect1.x1, rect1.y1, rect1.x2, rect1.y2), (rect2.x1, rect2.y1, rect2.x2, rect2.y2))
  
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
    line_num = re.finditer("(\d+)", a) 
    for i in line_num:
        if(len(i.groups())):
            number = int(i.group(1))
            location = i.span(1)
            num_pair = [number, row, location]
            numbers.append(num_pair)
        
    line_sym = re.finditer("([^\d\.])", a) 
    for i in line_sym:
        if(len(i.groups())):
            symbol = i.group(1)
            location = i.span(1)
            sym_pair = [symbol, row, location]
            symbols.append(sym_pair)
        
    a = f.readline()
    row += 1

from collections import namedtuple
RECT_NAMEDTUPLE = namedtuple('RECT_NAMEDTUPLE', 'x1 y1 x2 y2')

sum = 0
powers = 0
for symbol in symbols:
    sym_row = symbol[1]
    sym_loc = symbol[2]

    overlaps = [] 
    for number in numbers:
        row = number[1]
        if sym_row >= row-1 and sym_row <= row+1: #limit matches. unnecessary optimization
            num = number[0]
            row = number[1]
            loc = number[2]

            sym_rectangle = RECT_NAMEDTUPLE(sym_loc[0]-1, sym_row-1, sym_loc[1], sym_row+1)
            num_rectangle = RECT_NAMEDTUPLE(loc[0], row, loc[1]-1, row)
            if is_overlapping_2D(sym_rectangle, num_rectangle):
                sum += num
                
                if symbol[0] == "*":
                    overlaps.append(num)
    
    if len(overlaps) == 2:
       powers += reduce(mul, overlaps)

print(f"sum: {sum}")
print(f"power: {powers}")