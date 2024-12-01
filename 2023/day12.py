from utils import read_file_to_list
#from more_itertools import distinct_permutations
#from functools import cache
import time

'''
def is_valid_arrangement(arrangement, groups):
    broken_spring_groups = [x for x in arrangement.split(".") if x]
    if len(broken_spring_groups) != len(groups):
        return False
    for i in range(len(groups)):
        if len(broken_spring_groups[i]) != groups[i]:
            return False
    return True


def number_of_possible_arrangements(damaged_record):
    springs = damaged_record.split(" ")[0]
    contiguous_groups = [int(i) for i in damaged_record.split(" ")[1].split(",")]
    unknown_damaged_springs = sum(contiguous_groups) - springs.count("#")
    unknown_operational_springs = springs.count("?") - unknown_damaged_springs
    output = 0
    for unknown_arrangement in distinct_permutations("#" * unknown_damaged_springs + "." * unknown_operational_springs):
        spring_arrangement = springs
        for c in unknown_arrangement:
            spring_arrangement = spring_arrangement.replace("?", c, 1)
        if is_valid_arrangement(spring_arrangement, contiguous_groups):
            output += 1
    return output
'''

cache = {}
def number_of_possible_arrangements_recursive(springs: str, groups: tuple):
    global cache
    if (springs, groups) in cache.keys():
        return cache[(springs, groups)]

    if not groups:
        if "#" not in springs:
            return 1
        else:
            return 0

    if not springs:
        return 0

    next_character = springs[0]
    next_group = groups[0]
    
    def operational():
        return number_of_possible_arrangements_recursive(springs[1:], groups)

    def broken():
        this_group = springs[:next_group]
        this_group = this_group.replace("?", "#")

        if this_group != "#" * next_group:
            return 0
        
        if len(springs) == next_group:
            if len(groups) == 1:
                return 1
            else:
                return 0
        
        if springs[next_group] in ".?":
            return number_of_possible_arrangements_recursive(springs[next_group+1:], groups[1:])
        return 0

    output = 0
    if next_character == ".":
        output += operational()
    if next_character == "#":
        output += broken()
    if next_character == "?":
        output += operational() + broken()

    cache.update({(springs, groups) : output})
    return output
    

if __name__ == "__main__":

    puzzle_input = read_file_to_list("inputs/12/input.txt")
    sum_of_possible_arrangements = 0

    for line in puzzle_input:
        springs, groups_str = line.split(" ")
        contiguous_groups = tuple(int(i) for i in groups_str.split(","))
        sum_of_possible_arrangements += number_of_possible_arrangements_recursive(springs, contiguous_groups)

    print("Part 1:", sum_of_possible_arrangements)

    #----------------------------------------------------------------

    sum_of_possible_arrangements_2 = 0

    for line in puzzle_input:
        springs, groups_str = line.split(" ")
        springs = "?".join([springs] * 5)
        groups_str = ",".join([groups_str] * 5)
        contiguous_groups = tuple(int(i) for i in groups_str.split(","))

        sum_of_possible_arrangements_2 += number_of_possible_arrangements_recursive(springs, contiguous_groups)

    print("Part 2:", sum_of_possible_arrangements_2)