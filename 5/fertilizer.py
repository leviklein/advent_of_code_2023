import re
import pathlib

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

        while(len(table) < source+length-1):
            table[len(table)] = len(table)

        for i in range(length):
            table[source+i] = dest+i

        row += 1
        line = file[row]
    
    MAPPINGS.append(table)
    return row

def create_data_table():
    for seed in range(len(MAPPINGS[0])):
        entry = [seed]
        for i in MAPPINGS:
            entry.append(i.get(entry[-1], entry[-1]))

        DATA_TABLE.append(entry)
    


if __name__ == "__main__":
    script_path = str(pathlib.Path(__file__).parent.resolve()) + "/"
    f = open(script_path + "input.txt", "r")
    a = f.read().split('\n')


    target_seeds = re.findall("\d+", a[0])

    row = 1
    while row < len(a):
        if(a[row].find("map:") > 0):
            row = process_input(a, row+1)
        row+=1

    create_data_table()

    # print(MAPPINGS)
    # print(DATA_TABLE)

    location_seed = {}
    for seed in target_seeds:
        seed = int(seed)
        location = DATA_TABLE[seed][-1]
        location_seed[location] = seed

    
    lowest_seed_location = next(iter(sorted(location_seed)))
    print(f"lowest_seed_location: {lowest_seed_location}")

    pass