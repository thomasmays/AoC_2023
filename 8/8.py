import itertools

input_file = r"C:\Users\thomas.mays\OneDrive - Arup\Python Projects\Advent of Code 2023\8\input.csv"

with open(input_file) as f:
    input_data = f.read().split('\n')

route = input_data[0]
nodes = input_data[2:]

map = {}
for node in nodes:
    src, directions = node.split(" = ")[0], node.split(" = ")[1]
    map[src] = directions[1:-1].split(', ')

count = 0
loc = 'AAA'

while loc != 'ZZZ':
    for order in itertools.cycle(route):
        if order == 'L':
            loc = map[loc][0]
        else:
            loc = map[loc][1]
        count += 1

        if loc == 'ZZZ':
            break 

print(count)