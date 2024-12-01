from utils import read_file_to_list


def area(points):
    # Shoelace formula
    total = 0
    for i in range(len(points)-1):
        x1 = points[i][1]
        y1 = points[i][0]
        x2 = points[i+1][1]
        y2 = points[i+1][0]
        total += x1*y2 - x2*y1
    x1 = points[-1][1]
    y1 = points[-1][0]
    x2 = points[0][1]
    y2 = points[0][0]
    total += x1*y2 - x2*y1
    return total/2



if __name__ == "__main__":
    puzzle_input = read_file_to_list("inputs/18/input.txt")
    direction_dict = {"R" : (0, 1), "L" : (0, -1), "U" : (-1, 0), "D" : (1, 0)}

    y, x = 0, 0
    points = [(y, x)]
    boundary_points = 0
    for line in puzzle_input:
        direction, length, hex_color = line.split(" ")
        boundary_points += int(length)
        y += direction_dict[direction][0] * int(length)
        x += direction_dict[direction][1] * int(length)
        points.append((y, x))
    
    # pick's theorem
    interior_points = area(points) - boundary_points/2 + 1
    print("part 1", int(interior_points + boundary_points))

#--------------------------------------------------------------------
    
    y, x = 0, 0
    points = [(y, x)]
    boundary_points = 0
    hex_direction = {"0":"R", "1":"D", "2":"L", "3":"U"}
    for line in puzzle_input:
        direction, length, hex_color = line.split(" ")
        length = int(hex_color[2 : -2], base=16)
        direction = hex_direction[hex_color[-2]]
        boundary_points += int(length)
        y += direction_dict[direction][0] * int(length)
        x += direction_dict[direction][1] * int(length)
        points.append((y, x))
    
    # pick's theorem
    interior_points = area(points) - boundary_points/2 + 1
    print("part 2", int(interior_points + boundary_points))

