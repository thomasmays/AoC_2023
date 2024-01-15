import pandas as pd

input_file = r"C:\Users\thomas.mays\OneDrive - Arup\Python Projects\Advent of Code 2023\11\input.csv"

with open(input_file) as f:
    input_data = f.read().split('\n')

image = []
for i, line in enumerate(input_data):
    new_line = list(line)
    image.append(new_line)
image = pd.DataFrame(image)
image.columns = [float(x) for x in list(image.columns)]

for index, row in image.iterrows():
    if '#' not in row.unique():
        image.loc[index-0.5, :] = ['.']
image = image.sort_index().reset_index(drop=True)

for index, col in image.items():
    if '#' not in col.unique():
        image[index-0.5] = ['.']*len(col)

image = image.reindex(sorted(image.columns), axis=1)
image.columns = range((image.shape[1]))

galaxy_locs = {}
galaxy_num = 1
for row_index, row in image.iterrows():
    for col_index, value in enumerate(row):
        if value == '#':
            galaxy_locs[galaxy_num] = (row_index, col_index)
            galaxy_num = galaxy_num + 1
            
path_lengths = {}
for src_galaxy_num, src_galaxy_loc in galaxy_locs.items():
    dest_galaxy_nums = list(range(src_galaxy_num+1, len(galaxy_locs)+1))
    dest_galaxy_locs = []
    for dest_galaxy_num in dest_galaxy_nums:
        dest_galaxy_locs.append(galaxy_locs[dest_galaxy_num])
    dest_galaxies = dict(zip(dest_galaxy_nums, dest_galaxy_locs))

    for dest_galaxy_num, dest_galaxy_loc in dest_galaxies.items():
        row_steps = dest_galaxy_loc[0] - src_galaxy_loc[0]
        col_steps = dest_galaxy_loc[1] - src_galaxy_loc[1]
        path_lengths[str(src_galaxy_num) + " & " + str(dest_galaxy_num)] = abs(row_steps) + abs(col_steps)

print(sum(path_lengths.values()))