from utils import read_file_to_list
from itertools import combinations
from collections import Counter

def expand_universe(universe: list) -> list:
    """Returns a universe where every row or column without a galaxy(#) is twice as big"""
    expanded_universe = []
    
    empty_columns = []
    for col in range(len(universe[0])):
        if all(line[col] == "." for line in universe):
            empty_columns.append(col)

    for line in universe:
        line = list(line)
        for j, i in enumerate(empty_columns):
            line.insert(i+j, ".")
        line = "".join(line)
        expanded_universe.append(line)
        if "#" not in line:
            expanded_universe.append(line)
    return expanded_universe


def expand_universe_million(universe: list) -> list:
    """Returns a universe where every row or column without a galaxy(#) is 1_000_000 times as big
    
    empty rows and columns are actually replaced with an M"""
    expanded_universe = []

    empty_columns = []
    for col in range(len(universe[0])):
        if all(line[col] == "." for line in universe):
            empty_columns.append(col)

    for line in universe:
        line = list(line)
        for i in empty_columns:
            line[i] = "M"
        line = "".join(line)

        if "#" not in line:
            expanded_universe.append("M" * len(line))
        else:
            expanded_universe.append(line)

    return expanded_universe
        

def list_of_galaxies(universe: list) -> list[tuple]:
    galaxies = []
    for y, line in enumerate(universe):
        for x, c in enumerate(line):
            if c == "#":
                galaxies.append((y, x))
    return galaxies


if __name__ == "__main__":
    puzzle_input = read_file_to_list("inputs/11/input.txt")
    expanded_universe = expand_universe(puzzle_input)
    galaxy_positions = list_of_galaxies(expanded_universe)
    galaxy_pairs = combinations(galaxy_positions, 2)

    sum_of_path_lengths = 0
    for i in galaxy_pairs:
        g1 = i[0]
        g2 = i[1]
        sum_of_path_lengths += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    print("Part 1:", sum_of_path_lengths)

    #-----------------------------------------------------------------------------------

    expanded_universe_M = expand_universe_million(puzzle_input)
    galaxy_positions_M = list_of_galaxies(expanded_universe_M)
    galaxy_pairs_M = combinations(galaxy_positions_M, 2)

    sum_of_path_lengths_2 = 0
    for i in galaxy_pairs_M:
        g1 = i[0]
        g2 = i[1]
        M_size = 1_000_000

        vertical_count = Counter([line[g1[1]] for line in expanded_universe_M[g1[0] + 1 : g2[0] + 1]])
        horizontal_count = Counter(expanded_universe_M[g1[0]][min(g1[1], g2[1]) + 1 : max(g1[1], g2[1]) + 1])
        
        vertical_path_length = vertical_count["M"] * M_size + vertical_count["#"] + vertical_count["."]
        horizontal_path_length = horizontal_count["M"] * M_size + horizontal_count["#"] + horizontal_count["."]
        sum_of_path_lengths_2 += vertical_path_length + horizontal_path_length

    print("Part 2:", sum_of_path_lengths_2)

# part 2 is slow, using this method would be faster: 
# https://www.reddit.com/r/adventofcode/comments/18fp13u/2023_day_11_animated_visualization/