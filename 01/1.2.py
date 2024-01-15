import re

input_file = r"C:\Users\thomas.mays\OneDrive - Arup\Python Projects\Advent of Code 2023\1\input.csv"

with open(input_file) as f:
    input_data = f.read().split('\n')

result_list = []
number_words = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
                'nine': '9'}

for line in input_data:
    replace_indices = {}

    for word in number_words:
        ix = [m.start() for m in re.finditer(word, line)]
        if len(ix) > 0:
            replace_indices[word] = ix

    replaced_line = line
    for word, indices in replace_indices.items():
        for index in indices:
            replaced_line = replaced_line[:index] + number_words[word] + replaced_line[index+1:]

    numbers = None
    for character in replaced_line:
        try:
            int(character)
            if numbers == None:
                numbers = character
            else:
                numbers += character
        except ValueError:
            pass

    first_last_numbers = numbers[0] + numbers[-1]
    combined_numbers = int(first_last_numbers)
    result_list.append(combined_numbers)

print(sum(result_list))