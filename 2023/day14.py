from utils import read_file_to_list


def total_load_north(puzzle):
    load_per_rock = [len(puzzle)] * len(puzzle[0])
    total_load = 0
    for i, line in enumerate(puzzle, start=1):
        for j, c in enumerate(line):
            if c == "O":
                total_load += load_per_rock[j]
                load_per_rock[j] -= 1
            if c == "#":
                load_per_rock[j] = len(puzzle) - i
    return total_load


def calculate_load(puzzle):
    total_load = 0
    for i, line in enumerate(puzzle):
        for j, c in enumerate(line):
            if c == "O":
                total_load += len(puzzle) - i
    return total_load


def tilt_north(puzzle):
    open_space = [0] * len(puzzle[0])
    puzzle = [list(line) for line in puzzle]
    for i, line in enumerate(puzzle):
        for j, c in enumerate(line):
            if c == "O":
                puzzle[i][j] = "."
                puzzle[open_space[j]][j] = "O"
                open_space[j] += 1
            if c == "#":
                open_space[j] = i + 1 
    puzzle = ["".join(line) for line in puzzle]
    return puzzle


def tilt_south(puzzle):
    open_space = [0] * len(puzzle[0])
    puzzle = [list(line) for line in puzzle[::-1]]
    for i, line in enumerate(puzzle):
        for j, c in enumerate(line):
            if c == "O":
                puzzle[i][j] = "."
                puzzle[open_space[j]][j] = "O"
                open_space[j] += 1
            if c == "#":
                open_space[j] = i + 1 
    puzzle = ["".join(line) for line in puzzle[::-1]]
    return puzzle


def tilt_west(puzzle):
    puzzle = [list(line) for line in puzzle]
    for i, line in enumerate(puzzle):
        open_space = 0
        for j, c in enumerate(line):
            if c == "O":
                puzzle[i][j] = "."
                puzzle[i][open_space] = "O"
                open_space += 1
            if c == "#":
                open_space = j + 1 
    puzzle = ["".join(line) for line in puzzle]
    return puzzle


def tilt_east(puzzle):
    puzzle = [list(line[::-1]) for line in puzzle]
    for i, line in enumerate(puzzle):
        open_space = 0
        for j, c in enumerate(line):
            if c == "O":
                puzzle[i][j] = "."
                puzzle[i][open_space] = "O"
                open_space += 1
            if c == "#":
                open_space = j + 1 
    puzzle = ["".join(line[::-1]) for line in puzzle]
    return puzzle
    
                
def spin_cycle(puzzle):
    puzzle = tilt_north(puzzle)
    puzzle = tilt_west(puzzle)
    puzzle = tilt_south(puzzle)
    puzzle = tilt_east(puzzle)
    return puzzle

if __name__ == "__main__":
    puzzle_input = read_file_to_list("inputs/14/input.txt")
    print("part 1:", total_load_north(puzzle_input))

    puzzle_spin = spin_cycle(puzzle_input)
    prev_cycles = []
    while puzzle_spin not in prev_cycles:
        prev_cycles.append(puzzle_spin)
        puzzle_spin = spin_cycle(puzzle_spin)
    loop_start = prev_cycles.index(puzzle_spin)
    loop = prev_cycles[loop_start:]
    num_cycles = 1_000_000_000 - (loop_start + 1)
    puzzle_spin_B = loop[num_cycles % len(loop)]

    print("part 2:", calculate_load(puzzle_spin_B))