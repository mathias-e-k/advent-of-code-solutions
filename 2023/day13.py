from utils import read_file_to_list_double_nl

def line_of_reflection(pattern: str) -> int:
    horizontal_lines = pattern.split()
    vertical_lines = []
    for i in range(len(horizontal_lines[0])):
        vertical_line = ""
        for line in horizontal_lines:
            vertical_line += line[i]
        vertical_lines.append(vertical_line)
    horizontal_reflection_lines = [i+1 for i in range(len(horizontal_lines)-1) if horizontal_lines[i] == horizontal_lines[i+1]]
    vertical_reflection_lines = [i+1 for i in range(len(vertical_lines)-1) if vertical_lines[i] == vertical_lines[i+1]]

    for i in horizontal_reflection_lines:
        if all(horizontal_lines[i-1-j] == horizontal_lines[i+j] for j in range(1, min(i, len(horizontal_lines)-i))):
            return i*100
    
    for i in vertical_reflection_lines:
        if all(vertical_lines[i-1-j] == vertical_lines[i+j] for j in range(1, min(i, len(vertical_lines)-i))):
            return i
    print("erm")
    return 0


def line_of_reflection_with_smudge(pattern: str) -> int:
    horizontal_lines = pattern.split()
    vertical_lines = []
    for i in range(len(horizontal_lines[0])):
        vertical_line = ""
        for line in horizontal_lines:
            vertical_line += line[i]
        vertical_lines.append(vertical_line)

    horizontal_reflection_lines = []
    vertical_reflection_lines = []
    for i in range(len(horizontal_lines)-1):
        if sum(1 for i in zip(horizontal_lines[i], horizontal_lines[i+1]) if i[0] != i[1]) <= 1:
            horizontal_reflection_lines.append(i+1)
    for i in range(len(vertical_lines)-1):
        if sum(1 for i in zip(vertical_lines[i], vertical_lines[i+1]) if i[0] != i[1]) <= 1:
            vertical_reflection_lines.append(i+1)
    
    for i in horizontal_reflection_lines:
        differences = 0
        for j in range(min(i, len(horizontal_lines)-i)):
            differences += sum(1 for k in zip(horizontal_lines[i-1-j], horizontal_lines[i+j]) if k[0] != k[1])
        if differences == 1:
            return i*100
        
    for i in vertical_reflection_lines:
        differences = 0
        for j in range(min(i, len(vertical_lines)-i)):
            differences += sum(1 for k in zip(vertical_lines[i-1-j], vertical_lines[i+j]) if k[0] != k[1])
        if differences == 1:
            return i
    print(horizontal_reflection_lines, vertical_reflection_lines)
    return 0



if __name__ == "__main__":
    puzzle_input = read_file_to_list_double_nl("inputs/13/input.txt")
    
    part1_sum = sum(line_of_reflection(p) for p in puzzle_input)
    print("Part 1:", part1_sum)

    part2_sum = sum(line_of_reflection_with_smudge(p) for p in puzzle_input)
    print("Part 2:", part2_sum)
    
