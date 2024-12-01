from utils import read_file_to_list
import collections

def connected_to_start(full_map: list) -> list[tuple[tuple, str]]:
    """Returns the position of both pipes connected to S, and where to go next"""
    global pipe_types
    for i, line in enumerate(full_map):
        if "S" in line:
            j = line.find("S")
            S_position = (i, j)
            break
    
    adjacent_pipes = []
    # north
    adjacent_pipes.append(((S_position[0]-1, S_position[1]), "south"))
    # south
    adjacent_pipes.append(((S_position[0]+1, S_position[1]), "north"))
    # west
    adjacent_pipes.append(((S_position[0], S_position[1]-1), "east"))
    # east
    adjacent_pipes.append(((S_position[0], S_position[1]+1), "west"))

    output = []
    start_direction = []
    for pipe in adjacent_pipes:                 # naming variables is so difficult
        position = pipe[0]
        came_from = pipe[1]
        pipe_type = full_map[position[0]][position[1]]
        going_to = list(pipe_types[pipe_type])
        
        if came_from in going_to:
            start_direction.append(came_from)
            going_to.remove(came_from)
            output.append((position, going_to[0]))
            replace_symbol(position)
    replace_symbol(S_position, start=start_direction)
    return output


def next_pipe(pipe_pos) -> tuple[tuple, str]:
    global pipe_map
    global pipe_types
    directions = {"south":(-1, 0), "north":(1, 0), "east":(0, -1), "west":(0, 1)}
    opposite_direction = {"north":"south", "south":"north", "west":"east", "east":"west"}
    came_from = opposite_direction[pipe_pos[1]]
    difference = directions[came_from]
    connected_pipe_pos = (pipe_pos[0][0] + difference[0], pipe_pos[0][1] + difference[1])
    next_pipe_pos = pipe_map[connected_pipe_pos[0]][connected_pipe_pos[1]]
    try:
        going_to = list(pipe_types[next_pipe_pos])
    except:
        return (connected_pipe_pos, "END")
    going_to.remove(came_from)
    replace_symbol(connected_pipe_pos)
    return (connected_pipe_pos, going_to[0])


def replace_symbol(pos, start = None):
    """Replace symbols that are part of the loop with other symbols.
    
    This is required to count how many points are enclosed by the loop for part 2"""
    global pipe_map
    global pipe_types
    path_replacement = {"|":"V", "-":"H",
                        "L":"\\", "7":"\\",
                        "J":"/", "F":"/"}
    if start:
        opposite_direction = {"north":"south", "south":"north", "west":"east", "east":"west"}
        for p in pipe_types.items():
            if all(opposite_direction[i] in p[1] for i in start):
                new_char = p[0]
                pipe_map[pos[0]] = pipe_map[pos[0]][0 : pos[1]] + new_char + pipe_map[pos[0]][pos[1]+1 : ]
                break

    try:
        new_char = path_replacement[pipe_map[pos[0]][pos[1]]]
        pipe_map[pos[0]] = pipe_map[pos[0]][0 : pos[1]] + new_char + pipe_map[pos[0]][pos[1]+1 : ]
    except KeyError:
        print("eeh")
        return


def is_enclosed(pos) -> bool:
    """Checks if a point is enclosed in the loop by counting the number of walls to the right of the point."""
    global pipe_map
    pipe_counter = collections.Counter(pipe_map[pos[0]][pos[1]:])
    vertical_pipes = pipe_counter["V"]
    corner1 = pipe_counter["/"]
    corner2 = pipe_counter["\\"]
    walls_passed = vertical_pipes + corner1//2 + corner2//2
    if walls_passed % 2 == 0:
        return False
    else:
        return True


if __name__ == "__main__":
    pipe_map = read_file_to_list("inputs/10/input.txt")
    pipe_types = {"|":("south", "north"), "-":("east", "west"), 
                  "L":("north", "east"), "J":("north", "west"), 
                  "7":("south", "west"), "F":("south", "east"), 
                  ".":("ground", "ERR"), "S":("start", "start")}


    current_positions = connected_to_start(pipe_map)
    steps = 1
    while not current_positions[0][0] == current_positions[1][0]:
        current_positions = [next_pipe(current_positions[i]) for i in range(len(current_positions))]
        steps += 1
    print("part 1:", steps)


    new_symbols = ["V", "H", "\\", "/"]
    enclosed_tiles = 0
    for i, line in enumerate(pipe_map):
        for j, symbol in enumerate(line):
            if symbol in new_symbols:
                continue
            if is_enclosed((i,j)):
                enclosed_tiles += 1
    print("part 2:", enclosed_tiles)
