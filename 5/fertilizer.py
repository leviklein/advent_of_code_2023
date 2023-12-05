import re
import pathlib
import sys

# Global vars
DATA_TABLE = [] # [seed, soil, fertilizer, water, light, temperature, humidity, location]
MAPPINGS = []

def process_input(file, row):
    table = []

    line = file[row]
    while line != '':
        values = re.findall("\d+", line)
        dest = int(values[0])
        source = int(values[1])
        length = int(values[2])
        

        # table[source] = {"dest": dest, "len": length}
        table.append([dest, source, source+length-1])
        row += 1
        line = file[row]

    MAPPINGS.append(sorted(table, key=lambda x: x[1]))
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

def get_table_ranges(table):
    ranges = []
    for entry in table.items():
        ranges.append((entry[0], entry[0] + entry[1]["len"]))
        pass

def is_instersecting(source_entry, dest_entry):
    return source_entry[2]  >= dest_entry[1] and \
           dest_entry[2] >= source_entry[1] 

def get_intersections(source_entry, dest_entry):
    intersection_1 = max(source_entry[1], dest_entry[1])
    intersection_2 = min(source_entry[2], dest_entry[2])
    intersection = [dest_entry[0], intersection_1, intersection_2]
    return intersection

def subtract_ranges(entry, intersection):
    new_range = [ x for x in entry ]
    if entry[1] < intersection[1]:
        new_range[2] = min(entry[2], intersection[1]-1)
    elif entry[2] > intersection[2]:
        new_range[1] = max(entry[1], intersection[2]+1)
    
    if new_range[2] < new_range[1]:
        new_range = []
    return new_range

def get_lower_entry(entry1, entry2):
    if entry1[1] < entry2[1]:
        return 0
    else:
        return 1

def create_new_mapping(source_table, dest_table):
    new_mapping = []

    i = 0# len(source_table)
    j = 0# len(dest_table)
    while i < len(source_table):
        while j < len(dest_table):
            if is_instersecting(source_table[i], dest_table[j]):
                intersection_entry = get_intersections(source_table[i], dest_table[j])
                entry1 = subtract_ranges(source_table[i], intersection_entry)
                entry2 = subtract_ranges(dest_table[j], intersection_entry)
                new_mapping += intersection_entry, entry1, entry2
                i+=1
                j+=1
                continue
            else:
                idx = get_lower_entry(source_table[i], dest_table[j])
                new_mapping += [[source_table[i], dest_table[j]][idx]]
                if idx:
                    j += 1
                else:
                    i += 1
                continue
        
        for entry in new_mapping:
            if is_instersecting(source_table[i], entry):
                intersection_entry = get_intersections(source_table[i], entry)
                entry1 = subtract_ranges(source_table[i], intersection_entry)
                new_mapping += entry1
                i+=1
                continue
        new_mapping += [source_table[i]]

        i+=1
        
    pass
    return sorted(new_mapping, key=lambda x: x[1])



    # get_table_ranges(source_table)

    # for dest_entry in dest_table:
    #     dest_entry.keys()
def get_answer():
    answer = MAPPINGS[0]
    for i in range(0, len(MAPPINGS)-1):
        answer = create_new_mapping(MAPPINGS[i], MAPPINGS[i+1])
    return answer

def get_seed_location(seed):
    return get_mapping_across_tables(seed, 0, 6)


if __name__ == "__main__":
    script_path = str(pathlib.Path(__file__).parent.resolve()) + "/"
    f = open(script_path + "input.txt", "r")
    f = open(script_path + "test_input.txt", "r")
    a = f.read().split('\n')

    input = [ int(x) for x in re.findall("\d+", a[0]) ]
    target_seeds = input

    row = 1
    while row < len(a):
        if(a[row].find("map:") > 0):
            row = process_input(a, row+1)
        row+=1

    answer = get_answer()
    # lowest_seed_location = sys.maxsize
    # i = 0
    # while i < len(input):
    #     for seed in range(input[i], input[i] + input[i+1]):
    #         location = get_seed_location(seed)
    #         lowest_seed_location = location if location < lowest_seed_location else lowest_seed_location
    #     i += 2

    # print(f"lowest_seed_location: {lowest_seed_location}")

    pass