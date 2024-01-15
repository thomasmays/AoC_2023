import pandas as pd
import numpy as np 

def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return value

def is_int(value):
    if type(value) == int:
        return True
    else:
        return False

def is_star(value):
    if value == '*':
        return True
    else:
        return False


input_file = r"C:\Users\thomas.mays\OneDrive - Arup\Python Projects\Advent of Code 2023\3\input.csv"

with open(input_file) as f:
    input_data = f.read().split('\n')

input_data = pd.DataFrame([list(row) for row in input_data])
converted_data = input_data.map(convert_to_int)
star_tf = converted_data.map(is_star)

star_locs = []
for row_num, row in star_tf.iterrows():
    cols = row.index[row == True]
    
    if len(cols) > 0:
        for col in cols:
            star_locs.append([row_num, col])

gear_ratios = []
for coords in star_locs:
    row, col = coords[0], coords[1]

    if row != 0:
        start_row = row-1
    else:
        start_row = row

    if row == len(converted_data)-1:
        end_row = row+1  
    else:
        end_row = row+2

    if col != 0:
        start_col = col-1
    else:
        start_col = col
    
    if col != len(converted_data.columns)-1:
        end_col = col+2
    else: 
        end_col = col+1

    sub_df = converted_data.iloc[start_row:end_row,start_col:end_col]

    numbers = []
    for row in list(sub_df.index):
        for col in list(sub_df.columns):
            if type(sub_df.loc[row,col]) == int:
                # find start
                j = -1
                try:
                    while type(converted_data.loc[row, col+j]) == int:  # go left
                        j -= 1
                except KeyError:
                    pass
                pointer_start = col+j+1

                # find end
                k = 1
                try:
                    while type(converted_data.loc[row, col+k]) == int:  # go right
                        k += 1
                except KeyError:
                    pass
                pointer_end = col+k

                new_number_df = converted_data.iloc[row, pointer_start:pointer_end]
                numbers.append(int("".join([str(x) for x in new_number_df])))

                if list(sub_df.columns).index(col) == 1:  # number is in middle, next row
                    break
            else:
                continue
    
    numbers = pd.unique(pd.Series(numbers))
    if len(numbers) == 2:
        gear_ratios.append(numbers[0] * numbers[1])

print(sum(gear_ratios))