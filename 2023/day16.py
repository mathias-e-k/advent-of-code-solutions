from utils import read_file_to_list

def in_grid(y, x, height, width) -> bool:
    if y not in range(height):
        return False
    if x not in range(width):
        return False
    return True


def count_energized_tiles(grid: list, starting_position: tuple) -> int:
    
    GRID_HEIGHT = len(grid)
    GRID_WIDTH = len(grid[0])
    energized_tiles_grid = [[""] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    move =  {"R" : (0, 1), "L" : (0, -1), "U" : (-1, 0), "D" : (1, 0)}

    queue = [starting_position]
    while queue:

        queue_item = queue.pop(0)
        y, x = queue_item[0], queue_item[1]
        direction = queue_item[2]
        
        while True:

            # Currently outside grid, go to next item in queue
            if not in_grid(y, x, GRID_HEIGHT, GRID_WIDTH):
                break
            
            # Have already traveled this path, go to next item in queue
            if direction in energized_tiles_grid[y][x]:
                break
            energized_tiles_grid[y][x] += direction
            
            # Vertical splitter
            if grid[y][x] == "|":
                # Ran into the side of vertical splitter, add two items to queue and go to next item in queue
                if direction in "LR":
                    queue.append((y, x, "U"))
                    queue.append((y, x, "D"))
                    break
            
            # Horizontal splitter
            if grid[y][x] == "-":
                # Ran into the bottom or top of horizontal splitter, add two items to queue and go to next item in queue
                if direction in "UD":
                    queue.append((y, x, "L"))
                    queue.append((y, x, "R"))
                    break
            
            # Mirror, change direction
            if grid[y][x] == "/":
                new_direction = {"U":"R", "D":"L", "L":"D", "R":"U"}
                direction = new_direction[direction]
            
            # Mirror, change direction
            if grid[y][x] == "\\":
                new_direction = {"U":"L", "D":"R", "L":"U", "R":"D"}
                direction = new_direction[direction]
            
            # Move 1 space
            y += move[direction][0]
            x += move[direction][1]

    energized_tiles = 0
    for line in energized_tiles_grid:
        for p in line:
            if p:
                energized_tiles += 1
    return energized_tiles

        




        



if __name__ == "__main__":
    puzzle_input = read_file_to_list("inputs/16/input.txt")
    starting_pos = (0, 0, "R")
    print("part 1:", count_energized_tiles(puzzle_input, starting_pos))

    #------------------------------------------------------------------------

    max_tiles = 0
    LEFT = 0
    RIGHT = len(puzzle_input[0]) - 1
    TOP = 0
    BOTTOM = len(puzzle_input) - 1
    for i in range(len(puzzle_input)):
        starting_pos_R = (i, LEFT, "R")
        starting_pos_L = (i, RIGHT, "L")
        tiles_R = count_energized_tiles(puzzle_input, starting_pos_R)
        tiles_L = count_energized_tiles(puzzle_input, starting_pos_L)
        if max(tiles_R, tiles_L) > max_tiles:
            max_tiles = max(tiles_R, tiles_L)
    for i in range(len(puzzle_input[0])):
        starting_pos_D = (TOP, i, "D")
        starting_pos_U = (BOTTOM, i, "U")
        tiles_D = count_energized_tiles(puzzle_input, starting_pos_D)
        tiles_U = count_energized_tiles(puzzle_input, starting_pos_U)
        if max(tiles_D, tiles_U) > max_tiles:
            max_tiles = max(tiles_D, tiles_U)
    print("part 2:", max_tiles)
    