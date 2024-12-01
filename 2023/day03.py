from utils import read_file_to_list


def find_next_number(line: str, start: int=0) -> list[int, int]:
    number_start = -1
    number_end = len(line) + 1
    schematic_line = line[start:]
    for pos, char in enumerate(schematic_line):
        if char.isdigit():
            number_start = start + pos
            break
    
    schematic_line = line[number_start:]
    for pos, char in enumerate(schematic_line):
        if not char.isdigit():
            number_end = number_start + pos
            break
    return [number_start, number_end]


def adjacent_to_symbol(adjacent_lines: list, number_pos: list[int, int]) -> bool:
    invalid_symbols = (".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    number_start = number_pos[0]
    number_end = number_pos[1]
    for line in adjacent_lines:
        for char in line[max(number_start-1, 0) : min(number_end+1, len(line))]:
            if char not in invalid_symbols:
                return True
    return False
            

def sum_part_numbers(current_lines, prev_lines, next_lines) -> int:
    total = 0
    for i in range(len(current_lines)):
        number_start, number_end = 0, 0
        adjacent_lines = [prev_lines[i], current_lines[i], next_lines[i]]
        while True:
            number_position = find_next_number(current_lines[i], number_end)
            number_start = number_position[0]
            number_end = number_position[1]
            if number_start == -1:
                break
            if adjacent_to_symbol(adjacent_lines, number_position):
                number = int(current_lines[i][number_start : number_end])
                total += number
    return total


def find_next_gear_symbol(line: str, start: int=0) -> int:
    gear_position = -1
    schematic_line = line[start:]
    for pos, char in enumerate(schematic_line):
        if char == "*":
            gear_position = start + pos
            break
    return gear_position


def is_close(num1, num2):
    if abs(num1 - num2) <= 1:
        return True
    else:
        return False
    

def find_adjacent_numbers(adjacent_lines: list, gear_pos: int) -> list:
    adjacent_numbers = []
    for line in adjacent_lines:
        number_start, number_end = 0, 0
        while True:
            number_position = find_next_number(line, start=number_end)
            number_start = number_position[0]
            number_end = number_position[1]
            if number_start == -1:
                break
            if is_close(gear_pos, number_start) or is_close(gear_pos, number_end-1):
                adjacent_numbers.append(int(line[number_start : number_end]))
    return adjacent_numbers


def sum_gear_ratios(current_lines, prev_lines, next_lines) -> int:
    total = 0
    for i in range(len(current_lines)):
        gear_position = -1
        for j in range(schematic_lines[i].count("*")):
            gear_position = find_next_gear_symbol(schematic_lines[i], start=gear_position+1)
            adjacent_lines = [prev_lines[i], schematic_lines[i], next_lines[i]]
            adjacent_numbers = find_adjacent_numbers(adjacent_lines, gear_position)
            if len(adjacent_numbers) == 2:
                total += adjacent_numbers[0] * adjacent_numbers[1]
    return total


if __name__ == "__main__":
    schematic_lines = read_file_to_list("inputs/03/input.txt")
    previous_lines = [""]
    previous_lines.extend(schematic_lines[0:-1].copy())
    next_lines = schematic_lines[1:].copy()
    next_lines.append("")
    print("part 1:", sum_part_numbers(schematic_lines, previous_lines, next_lines))

    # part 1 could also use the part 2 solution, could be better
    # just need to look for any symbol that isn't a number or period(.)
    print("part 2:", sum_gear_ratios(schematic_lines, previous_lines, next_lines))
        
            

