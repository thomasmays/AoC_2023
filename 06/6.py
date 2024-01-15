import pandas as pd
import math

input_file = r"C:\Users\thomas.mays\OneDrive - Arup\Python Projects\Advent of Code 2023\6\input.csv"

with open(input_file) as f:
    input_data = f.read().split('\n')

races = []
for i, line in enumerate(input_data):
    line = line.split(':')[1]
    line = line.split(' ')
    line = [x for x in line if x != ' ']
    line = [int(x) for x in line if x != '']
    races.append(line)

races = zip(races[0], races[1])

qty_wins = []
for race in races:
    time = race[0]
    record_distance = race[1]

    given_speed = pd.Series(range(0, time+1, 1))
    time_left_range = given_speed.iloc[::-1].reset_index(drop=True)

    distace_travelled = given_speed * time_left_range

    record_beaten = distace_travelled > record_distance
    qty_wins.append(record_beaten.values.sum())


print(math.prod(qty_wins))
