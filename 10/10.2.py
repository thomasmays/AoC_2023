import pandas as pd


def check_valid_adj(tile, dir):

    if dir == "up":  # up
        valid_tiles = ['F', '7', '|']
    elif dir == "left":  # left
        valid_tiles = ['L', '-', 'F']
    elif dir == "right":  # right
        valid_tiles = ['J', '-', '7']
    elif dir == "down":  # daan
        valid_tiles = ['|', 'J', 'L']
    
    if tile in valid_tiles:
        return True
    else:
        return False


input_file = r"C:\Users\thomas.mays\OneDrive - Arup\Python Projects\Advent of Code 2023\10\sample_input.csv"

with open(input_file) as f:
    input_data = f.read().split('\n')

pipe_map = []
for i, line in enumerate(input_data):
    new_line = list(line)
    pipe_map.append(new_line)

    try:
        starting_pos = (i, new_line.index('S'))
    except ValueError:
        pass

pipe_map = pd.DataFrame(pipe_map, columns=None)


# get surrounding tiles, find valid next step, set new loc and store path until reach start again
end_reached = False
curr_loc = starting_pos
path = [curr_loc]
while end_reached == False:
    row_start, row_end, col_start, col_end = None, None, None, None

    # # get surrounding tiles
    # if curr_loc[0] == 0:
    #     row_start = curr_loc[0]
    # if curr_loc[0] == pipe_map.shape[0]-1:
    #     row_end = curr_loc[0]+1
    # if curr_loc[1] == 0:
    #     col_start = curr_loc[1]
    # if curr_loc[1] == pipe_map.shape[1]-1:
    #     col_end = curr_loc[1]+1
 
    # if row_start == None: row_start = curr_loc[0]-1
    # if row_end == None: row_end = curr_loc[0]+2
    # if col_start == None: col_start = curr_loc[1]-1
    # if col_end == None: col_end = curr_loc[1]+2        
    
    #  surr_tiles = pipe_map.iloc[row_start:row_end, col_start:col_end]

    next_tile = None
    for dir in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
        row_adj, col_adj = dir[0], dir[1]

        try:
            next_coords = curr_loc[0]+row_adj, curr_loc[1]+col_adj
            tile = pipe_map.loc[next_coords]
        except KeyError:  # out of bounds
            continue

        if tile == '.':
            continue

        tile_valid = False
        if [row_adj, col_adj] == [-1, 0]:  # up
            dir = "up"
        elif [row_adj, col_adj] == [0, -1]:  # left
            dir = "left"
        elif [row_adj, col_adj] == [0, 1]:  # right
            dir = "right"
        elif [row_adj, col_adj] == [1, 0]:  # daan
            dir = "down"

        tile_valid_forward = check_valid_adj(tile, dir)
        tile_valid_backward = False
        if tile_valid_forward:
            if dir == "up": rev_dir = "down"
            elif dir == "down": rev_dir = "up"
            elif dir == "left": rev_dir = "right"
            elif dir == "right": rev_dir = "left"

            curr_tile_value = pipe_map.iloc[curr_loc[0], curr_loc[1]]
            if curr_tile_value == "S":
                tile_valid_backward = True
            else:
                tile_valid_backward = check_valid_adj(curr_tile_value, rev_dir)

        next_tile = None
        if tile_valid_forward and tile_valid_backward:
            if  len(path) == 1 or next_coords != path[-2]:  # make sure you're not going backwards
                next_tile = next_coords
                path.append(next_tile)
                break
        
    if not next_tile:  # should've reached the end
        end_reached = True
    else:
        curr_loc = next_tile


clean_pipe_map = pipe_map
for coord in path:
    clean_pipe_map.at[coord] = "*"




debug = 1