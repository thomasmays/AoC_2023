import pandas as pd

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

def is_sym(value):
    if type(value) == str:
        if value == '.':
            return False
        else:
            return True
    else:
        return False


input_file = r"C:\Users\thomas.mays\OneDrive - Arup\Python Projects\Advent of Code 2023\3\input.csv"

with open(input_file) as f:
    input_data = f.read().split('\n')

input_data = pd.DataFrame([list(row) for row in input_data])
converted_data = input_data.map(convert_to_int)
numbers_tf = converted_data.map(is_int)
symbol_tf = converted_data.map(is_sym)

num_ranges = {}
for i, row in converted_data.iterrows():
    num_ranges[i] = []
    start = None
    end = None

    for j, value in enumerate(row):
        if start == None and type(value) == int:
            start = j
        
        try:
            if start != None and type(row[j+1]) != int:
                end = j
                num_ranges[i].append([start, end]) 
                start = None
                end = None
        except KeyError:  # end of row
            if start != None:
                end = j
                num_ranges[i].append([start, end]) 
                start = None
                end = None

symbols = ['-','&','%','=','+','/','@','$','*','#']
valid_numbers = []
for row, numbers_list in num_ranges.items():
    for num_pair in numbers_list:
        start, end = num_pair[0], num_pair[1]

        if row != 0:
            start_row = row-1
        else:
            start
            start_row = row

        if row == len(converted_data)-1:
            end_row = row+1  
        else:
            end_row = row+2

        if start != 0:
            start_col = start-1
        else:
            start_col = start
        
        if end != len(converted_data.columns)-1:
            end_col = end+2
        else: 
            end_col = end+1

        sub_df = converted_data.iloc[start_row:end_row,start_col:end_col]

        if sub_df.isin(symbols).any(axis=None):
            number_df = converted_data.iloc[row,start:end+1]
            valid_numbers.append(int("".join([str(x) for x in number_df])))


print(sum(valid_numbers))