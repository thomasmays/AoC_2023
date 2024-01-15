import pandas as pd

input_file = r"C:\Users\thomas.mays\OneDrive - Arup\Python Projects\Advent of Code 2023\4\input.csv"

with open(input_file) as f:
    input_data = f.read().split('\n')

org_data = {}
total_score = 0

for line in input_data:
    winners, my_nums = line.split('|')[0], line.split('|')[1]
    game_no, winners = winners.split(':')[0], winners.split(':')[1]

    game_no = game_no.split(' ')[-1]

    my_nums = my_nums.split(' ')
    my_nums = [x for x in my_nums if x != ' ']
    my_nums = list(filter(None, my_nums))
    my_nums = pd.Series(my_nums)

    winners = winners.split(' ')
    winners = [x for x in winners if x != ' ']
    winners = list(filter(None, winners))
    winners = pd.Series(winners)

    rd_score = 0
    for winning_no in winners:
        if winning_no in my_nums.unique():
            if rd_score == 0:
                rd_score = 1
            else:
                rd_score = rd_score * 2
    
    total_score += rd_score

print(total_score)