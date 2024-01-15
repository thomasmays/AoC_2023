import itertools

input_file = r"C:\Users\thomas.mays\OneDrive - Arup\Python Projects\Advent of Code 2023\8\input.csv"

with open(input_file) as f:
    input_data = f.read().split('\n')

route = input_data[0]
nodes = input_data[2:]

map = {}
threads = {}
for node in nodes:
    start, directions = node.split(" = ")[0], node.split(" = ")[1]
    map[start] = directions[1:-1].split(', ')
    
    if start[-1] == 'A':
        threads[start] = start        

count = 0
all_z = False


for order in itertools.cycle(route):
    all_z = True

    for name, pos in threads.items():
        if order == 'L':
            threads[name] = map[pos][0]
        else:
            threads[name] = map[pos][1]

        if pos[-1] != 'Z':
            all_z = False
    
    if all_z == True:
        break
    
    count += 1
    if count%1000000 == 0:
        print(count)

print(count)