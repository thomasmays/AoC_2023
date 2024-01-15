import pandas as pd

input_file = r"C:\Users\thomas.mays\OneDrive - Arup\Python Projects\Advent of Code 2023\5\input.csv"

with open(input_file) as f:
    input_data = f.read().split('\n\n')

seeds = input_data[0].split(': ')[1].split(' ')
seeds = [int(x) for x in seeds]

maps = {}
for map in input_data[1:]:
    numbers = map.split(':')[1].split('\n')
    numbers = numbers[1:]

    new_array = []
    for row in numbers:
        new_row = row.split(' ')
        new_row = [int(x) for x in new_row]
        new_array.append(new_row)

    maps[map.split(':')[0]] = new_array

dest_list = []
for seed_num in seeds:
    dest_value = None
    
    for map_name, map in maps.items():
        if dest_value == None:
            src_value = seed_num
        else:
            src_value = dest_value

        for line in map:
            src_range = range(line[1],line[1]+line[2])
            dest_range = range(line[0],line[0]+line[2])

            if src_value in src_range:
                dest_value = dest_range[0] + (src_value - src_range[0])
                break

            dest_value = src_value    
    dest_list.append(dest_value)

print(min(dest_list))