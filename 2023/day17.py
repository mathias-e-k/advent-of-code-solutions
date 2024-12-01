from utils import read_file_to_list
import math
from collections import namedtuple


Node = namedtuple("Node", ["heat_loss", "coords", "path"])

def get_neighbours(n: Node) -> list:
    # Returns a list of positions: [((y, x), "Direction", n moves, added_heat_loss)]
    global puzzle_input
    puzzle_input_y_range = range(len(puzzle_input))
    puzzle_input_x_range = range(len(puzzle_input[0]))
    neighbour_directions = ["N", "S", "E", "W"]
    if n.path != "B":
        going = n.path[-1]
        opposite = {"N":"S", "S":"N", "E":"W", "W":"E"}
        neighbour_directions.remove(opposite[going])
        neighbour_directions.remove(going)
    
    output = []
    y = n.coords[0]
    x = n.coords[1]
    direction_to_coords = {"N":(-1, 0), "S":(1, 0), "E":(0, 1), "W":(0, -1)}

    for d in neighbour_directions:
        heat_loss = 0
        for i in range(1, 11):
            neighbour_y = y + i*direction_to_coords[d][0]
            neighbour_x = x + i*direction_to_coords[d][1]
            
            if neighbour_y not in puzzle_input_y_range:
                continue
            if neighbour_x not in puzzle_input_x_range:
                continue
            heat_loss += int(puzzle_input[neighbour_y][neighbour_x])
            if i < 4:
                continue
            output.append(((neighbour_y, neighbour_x), d, i, heat_loss))

    return output


def minimize_heat_loss(city_map):
    # Dijkstra's algorithm, kinda, maybe idk
    # https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm 

    # Actually i think im using BFS. BFS IS SLOW
    # https://en.wikipedia.org/wiki/Breadth-first_search

    starting_location = (0, 0)
    starting_heat_loss = 0
    starting_node = Node(starting_heat_loss, starting_location, "B")
    destination = (len(city_map) - 1, len(city_map[-1]) - 1)
    queue = [starting_node]
    unvisited_set = set()
    unvisited_set.add((starting_node.coords, starting_node.path[-1]))
    node_map = []
    for i in range(len(city_map)):
        line = []
        for j in range(len(city_map[0])):
            line.append([Node(math.inf, (i, j), "N"),
                         Node(math.inf, (i, j), "S"),
                         Node(math.inf, (i, j), "E"),
                         Node(math.inf, (i, j), "W")])
        for l in line:
            for n0 in l:
                unvisited_set.add((n0.coords, n0.path[-1]))
        node_map.append(line)
    node_map[0][0].clear()
    node_map[0][0].append(starting_node)

    while queue:
        queue.sort(key=lambda x: x.heat_loss)
        current_node = queue.pop(0)
        
        if current_node.coords == destination:
            return current_node.heat_loss, current_node.path
        
        neighbours = get_neighbours(current_node)

        for n in neighbours:
            if (n[0], n[1]) not in unvisited_set:
                continue

            y = n[0][0]
            x = n[0][1]

            heat_loss = current_node.heat_loss + n[3]
            n = Node(heat_loss, (y, x), current_node.path + n[1]*n[2])

            map_location = node_map[y][x]

            for m in map_location:
                if n.path[-1] != m.path[-1]:
                    continue

                # this new node is better, remove the old node
                if n.heat_loss < m.heat_loss:
                    if m in queue:
                        queue.remove(m)
                    map_location.remove(m)
                    queue.append(n)
                    map_location.append(n)

        unvisited_set.remove((current_node.coords, current_node.path[-1]))
        if len(unvisited_set) % 500 == 0:
            print(len(unvisited_set))


if __name__ == "__main__":
    puzzle_input = read_file_to_list("inputs/17/input.txt")
    # it works but it sucks
    print(minimize_heat_loss(puzzle_input))