import pandas as pd


def assign_type(hand):
    cards = hand["cards"]
    value_counts = cards.value_counts()

    try:
        value_counts.drop('J', inplace=True)
        if len(value_counts) <= 1:
            type = 1
        elif len(value_counts) == 2:
            # either full house or four of a kind
            if value_counts.iloc[0] == 3:
                type = 2
            elif value_counts.iloc[0] == 2 and value_counts.iloc[1] == 2:
                type = 3
            else:
                type = 2
        elif len(value_counts) == 3:
            # can only be 3kind
            type = 4
        elif len(value_counts) == 4:  # 1 pair
            type = 6
        else:
            print("this shouldn't happen")

        debug = 1

    except KeyError: # No J in hand
        if len(value_counts) == 1:
            type = 1
        elif len(value_counts) == 2:
            # either full house or four of a kind
            if value_counts.iloc[1] == 1:
                type = 2
            else:
                type = 3
        elif len(value_counts) == 3:
            # 2 pair or three of a kind
            if value_counts.iloc[0] == 3:  #3kind
                type = 4
            else:  # 2pair
                type = 5
        elif len(value_counts) == 4:  # 1 pair
            type = 6
        else:  # High card
            type = 7

    return type

def assign_card_values(hand):
    card_ranking = {"J": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                    "9": 9, "T": 10, "Q": 11, "K": 12, "A": 13}
    
    for i, card in enumerate(hand["cards"]):
        hand["card" + str(i+1)] = card_ranking[card]
    return hand


def sub_rank_cards(group):
    
    group = group.apply(assign_card_values, axis=1)
    group.sort_values(["card1", "card2", "card3", "card4", "card5"], ascending=False, inplace=True)   

    return group


input_file = r"C:\Users\thomas.mays\OneDrive - Arup\Python Projects\Advent of Code 2023\7\input.csv"

with open(input_file) as f:
    input_data = f.read().split('\n')

hands = []
for line in input_data:
    cards = pd.Series(list(line.split(' ')[0]))
    bid = int(line.split(' ')[1])
    hands.append({'cards': cards, 'bid': bid})

hands_df = pd.DataFrame(hands)

hands_df["type"] = hands_df.apply(assign_type, axis=1)
hands_df.sort_values("type", inplace=True)
type_groups = hands_df.groupby("type")
hands_df = type_groups.apply(sub_rank_cards)
hands_df["overall_rank"] = range(len(hands_df),0,-1)
hands_df.set_index("overall_rank", inplace=True)
hands_df["score"] = hands_df.index * hands_df["bid"]

print(hands_df["score"].sum())