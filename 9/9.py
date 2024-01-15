import pandas as pd

input_file = r"C:\Users\thomas.mays\OneDrive - Arup\Python Projects\Advent of Code 2023\9\input.csv"

with open(input_file) as f:
    input_data = f.read().split('\n')

extrapolated_values = []
for line in input_data:
    all_zeroes = False

    i = 0
    pattern = {i: [int(x) for x in line.split(' ')]}

    while all_zeroes == False:
        for j, value in enumerate(pattern[i]):
            try:
                new_value = pattern[i][j+1] - value    
            except IndexError:  # end of line
                break

            if j == 0:
                pattern[i+1] = [new_value]
            else:
                pattern[i+1].append(new_value) 
        
        unique_vals = pd.Series(pattern[i+1]).unique()
        if len(unique_vals) == 1 and unique_vals[0] == 0:
            all_zeroes = True
        else:
            i += 1
    
    pattern[len(pattern)-1].append(0)  # add a new 0 to last row
    for i in range(len(pattern)-1, 0, -1):
        pattern[i-1].append(pattern[i-1][-1] + pattern[i][-1])

    extrapolated_values.append(pattern[0][-1])  
        
print(sum(extrapolated_values))