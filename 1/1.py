input_file = r"C:\Users\thomas.mays\OneDrive - Arup\Python Projects\Advent of Code 2023\1\input.csv"

with open(input_file) as f:
    input_data = f.read().split('\n')

result_list = []
for line in input_data:

    numbers = None
    for character in line:
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
