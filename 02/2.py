input_file = r"C:\Users\thomas.mays\OneDrive - Arup\Python Projects\Advent of Code 2023\2\input.csv"

with open(input_file) as f:
    input_data = f.read().split('\n')

max_cube_counts = {'red': 12, 'green': 13, 'blue': 14}

output_result = 0
for line in input_data:
    game_no, sets = line.split(':')[0], line.split(':')[1]
    game_no = int(game_no.split(' ')[1])

    valid_game = True
    for set in sets.split(';'):
        for cube in set.split(','):
            qty, col = int(cube.split(' ')[1]), cube.split(' ')[2] 

            if qty > max_cube_counts[col]:
                valid_game = False

    if valid_game == True:
        output_result += game_no
    elif valid_game == False:
        pass

print(output_result)



