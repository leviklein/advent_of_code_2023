import re
import pathlib
import sys

# Global vars
DATA_TABLE = [] # [seed, soil, fertilizer, water, light, temperature, humidity, location]
MAPPINGS = [] 

def process_input(file, row):
    table = {}

    line = file[row]
    while line != '':
        values = re.findall("\d+", line)
        dest = int(values[0])
        source = int(values[1])
        length = int(values[2])

        table[source] = {"dest": dest, "len": length}
        row += 1
        line = file[row]
    
    MAPPINGS.append(table)
    return row

def get_lowest_index(num, sorted_list):
    lowest_index = sorted_list[0]
    for i in sorted_list:
        if num >= i:
            lowest_index = i
            continue
        break
    return lowest_index

def get_mapping_value(source, table):
    offset = 0
    lowest_index = get_lowest_index(source, sorted(table))
    if source >= lowest_index: 
        entry = table[lowest_index]
        if lowest_index + entry["len"] > source:
            offset = entry["dest"] - lowest_index

    dest = source + offset
    return dest
    
def get_mapping_across_tables(source, source_column,dest_column):
    dest = source
    for i in range(source_column, dest_column+1):
        dest = get_mapping_value(dest, MAPPINGS[i])
    
    return dest

def get_seed_location(seed):
    return get_mapping_across_tables(seed, 0, 6)
    

if __name__ == "__main__":
    script_path = str(pathlib.Path(__file__).parent.resolve()) + "/"
    f = open(script_path + "input.txt", "r")
    # f = open(script_path + "test_input.txt", "r")
    a = f.read().split('\n')

    input = [ int(x) for x in re.findall("\d+", a[0]) ]

    i = 0
    target_seeds = []
    while i < len(input):
        target_seeds.append(range(input[i], input[i]+input[i+1]-1))
        i += 2


    row = 1
    while row < len(a):
        if(a[row].find("map:") > 0):
            row = process_input(a, row+1)
        row+=1

    lowest_seed_location = sys.maxsize
    for seed_range in target_seeds:
        for seed in seed_range:
            location = get_seed_location(seed)
            lowest_seed_location = location if location < lowest_seed_location else lowest_seed_location
        print(f"lowest_seed_location in range [{seed_range}]: {lowest_seed_location}")
        

    print(f"lowest_seed_location: {lowest_seed_location}")

    pass