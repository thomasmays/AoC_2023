from math import prod

input_file = r"C:\Users\thomas.mays\OneDrive - Arup\Python Projects\Advent of Code 2023\2\input.csv"

with open(input_file) as f:
    input_data = f.read().split('\n')

max_cube_counts = {'red': 12, 'green': 13, 'blue': 14}

output_result = 0
for line in input_data:
    game_no, sets = line.split(':')[0], line.split(':')[1]
    game_no = int(game_no.split(' ')[1])

    colour_counts = {'red': 0, 'green': 0, 'blue': 0}

    for set in sets.split(';'):
        for cube in set.split(','):
            i, col = int(cube.split(' ')[1]), cube.split(' ')[2] 
            
            if colour_counts[col] < i:
                colour_counts[col] = i

    game_power = prod(colour_counts.values())
    output_result += game_power 

print(output_result)



