from utils import read_file_to_list_double_nl as read_file
import math

def next_location(starting_location, direction):
    global nodes
    return nodes[starting_location][direction]


def all_end_with_Z(locations: list) -> bool:
    for l in locations:
        if l[-1] != "Z":
            return False
    return True


if __name__ == "__main__":
    puzzle_input = read_file("inputs/08/input.txt")
    sequence = puzzle_input[0]
    sequence_length = len(sequence)
    nodes = {}
    for i in puzzle_input[1].split("\n"):
        i = i.split(" = ")
        current_location = i[0]
        destinations = i[1].split(", ")
        destination_left = destinations[0][1 :]
        destination_right = destinations[1][: -1]
        nodes.update({current_location: (destination_left, destination_right)})
    directions = {"L": 0, "R": 1}

    #---------------------------------------

    current_location = "AAA"
    steps = 0
    while current_location != "ZZZ":
        direction = directions[sequence[steps % sequence_length]]
        current_location = next_location(current_location, direction)
        steps += 1

    print("Part 1:", steps)

    #---------------------------------------
    
    locations = [key for key in nodes.keys() if key[-1] == "A"]
    loop_lengths = [0] * len(locations)

    steps = 0
    for i, location in enumerate(locations):
        current_location = location
        steps = 0
        while current_location[-1] != "Z":
            direction = directions[sequence[steps % sequence_length]]
            current_location = next_location(current_location, direction)
            steps += 1
        loop_lengths[i] = steps
    total_steps = 1
    for i in loop_lengths:
        total_steps = math.lcm(total_steps, i)
    print("Part 2:", total_steps)
