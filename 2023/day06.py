from utils import read_file_to_list
import math


def amount_of_ways_to_win(time: int, distance: int) -> int:
    # Quadratic formula
    
    a = -1
    b = time
    c = -distance
    x1 = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a
    x2 = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
    high_solution = math.floor(math.nextafter(x1, -math.inf))
    low_solution = math.ceil(math.nextafter(x2, math.inf))
    return high_solution - low_solution + 1


if __name__ == "__main__":

    puzzle_input = read_file_to_list("inputs/06/input.txt")
    time = [int(i) for i in puzzle_input[0].split(":")[1].split()]
    distance = [int(i) for i in puzzle_input[1].split(":")[1].split()]
    race_time_and_distance = list(zip(time, distance))

    num_of_ways_to_win = [amount_of_ways_to_win(race[0], race[1]) for race in race_time_and_distance]
    p = math.prod(num_of_ways_to_win)
    print("part 1:", p)

#----------------------------------------------------------------------------------------

    part2_time = int(puzzle_input[0].split(":")[1].replace(" ", ""))
    part2_distance = int(puzzle_input[1].split(":")[1].replace(" ", ""))
    part_2_solution = amount_of_ways_to_win(part2_time, part2_distance)
    print("part 2:", part_2_solution)
