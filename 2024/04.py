file_path = "inputs/04.txt"
with open(file_path) as file:
    lines = [line.rstrip() for line in file]

# Part 1
height = len(lines)
width = len(lines[0])
xmas_count = 0
for ypos, line in enumerate(lines):
    xpos = -1
    for x in range(line.count("X")):
        xpos = line.find("X", xpos + 1)
        can_go_right = xpos <= width - 4
        can_go_left = xpos >= 3
        can_go_down = ypos <= height - 4
        can_go_up = ypos >= 3

        # Right
        if can_go_right:
            xmas_str = "".join([lines[ypos][xpos + i] for i in range(4)])
            if xmas_str == "XMAS":
                xmas_count += 1

        # Left
        if can_go_left:
            xmas_str = "".join([lines[ypos][xpos - i] for i in range(4)])
            if xmas_str == "XMAS":
                xmas_count += 1

        # Down
        if can_go_down:
            xmas_str = "".join([lines[ypos + i][xpos] for i in range(4)])
            if xmas_str == "XMAS":
                xmas_count += 1

        # Up
        if can_go_up:
            xmas_str = "".join([lines[ypos - i][xpos] for i in range(4)])
            if xmas_str == "XMAS":
                xmas_count += 1

        # Down right
        if can_go_down and can_go_right:
            xmas_str = "".join([lines[ypos + i][xpos + i] for i in range(4)])
            if xmas_str == "XMAS":
                xmas_count += 1

        # Down left
        if can_go_down and can_go_left:
            xmas_str = "".join([lines[ypos + i][xpos - i] for i in range(4)])
            if xmas_str == "XMAS":
                xmas_count += 1

        # Up right
        if can_go_up and can_go_right:
            xmas_str = "".join([lines[ypos - i][xpos + i] for i in range(4)])
            if xmas_str == "XMAS":
                xmas_count += 1

        # Up left
        if can_go_up and can_go_left:
            xmas_str = "".join([lines[ypos - i][xpos - i] for i in range(4)])
            if xmas_str == "XMAS":
                xmas_count += 1

print("Part1:", xmas_count)

# Part 2
height = len(lines)
width = len(lines[0])
x_mas_count = 0
for ypos, line in enumerate(lines):
    xpos = -1
    for x in range(line.count("A")):
        xpos = line.find("A", xpos + 1)
        can_go_right = xpos <= width - 2
        can_go_left = xpos >= 1
        can_go_down = ypos <= height - 2
        can_go_up = ypos >= 1

        if not (can_go_right and can_go_left and can_go_down and can_go_up):
            continue
        down_right = lines[ypos + 1][xpos + 1]
        down_left = lines[ypos + 1][xpos - 1]
        up_right = lines[ypos - 1][xpos + 1]
        up_left = lines[ypos - 1][xpos - 1]
        if down_right + down_left + up_left + up_right in ["MMSS", "SMMS", "SSMM", "MSSM"]:
            x_mas_count += 1

print("Part2:", x_mas_count)
