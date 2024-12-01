from queue import PriorityQueue

class Graph:
    def __init__(self, file, part) -> None:
        self.puzzle_input = open(file).read().strip().split("\n")
        self.height_range = range(len(self.puzzle_input))
        self.width_range = range(len(self.puzzle_input[0]))
        self.goal = (len(self.puzzle_input)-1, len(self.puzzle_input[-1])-1)
        self.part = part
        if self.part == 1:
            self.crucible_movement_range = range(1, 4)
        else:
            self.crucible_movement_range = range(1, 11)


    def neighbours(self, node):
        heat_loss = node[0]
        y, x = node[1]
        if node[2] == "UD":
            next_directions = ("L", "R")
        elif node[2] == "LR":
            next_directions = ("U", "D")
        elif node[2] == "S":
            next_directions = ("D", "R")
        else: 
            print(node[2])
            raise ValueError
        direction_to_coords = {"U":(-1, 0), "D":(1, 0), "L":(0, -1), "R":(0, 1)}
        output = []

        for d in next_directions:
            new_heat_loss = heat_loss
            for i in self.crucible_movement_range:
                new_y = y + i*direction_to_coords[d][0]
                new_x = x + i*direction_to_coords[d][1]
                if new_y not in self.height_range:
                    break
                if new_x not in self.width_range:
                    break
                new_heat_loss += int(self.puzzle_input[new_y][new_x])

                if self.part != 1 and i < 4:
                    continue

                if d in "LR":
                    output.append((new_heat_loss, (new_y, new_x), "LR"))
                elif d in "UD":
                    output.append((new_heat_loss, (new_y, new_x), "UD"))
        return output

    
def least_heat_loss(graph):
    # A* algorithm
    # https://www.redblobgames.com/pathfinding/a-star/introduction.html#more 

    todo = PriorityQueue()
    start = (0, (0, 0), "S")
    todo.put((0, start))
    heat_loss = dict()
    heat_loss[((0, 0), "UD")] = 0 
    heat_loss[((0, 0), "LR")] = 0 
    
    while todo:
        current = todo.get()[1]
        if current[1] == graph.goal:
            return current[0]
        
        for next in graph.neighbours(current):
            if next[1:] not in heat_loss or next[0] < heat_loss[next[1:]]:
                heat_loss[next[1:]] = next[0]
                priority = next[0] + (graph.goal[0] - next[1][0] + graph.goal[1] - next[1][1])*1
                todo.put((priority, next))

import time
if __name__ == "__main__":
    start = time.time()
    file = "inputs/17/input.txt"
    g1 = Graph(file, part=1)
    print("part 1:", least_heat_loss(g1))
    print("--- %s seconds ---" % (time.time() - start), "\n")

    start2 = time.time()
    g2 = Graph(file, part=2)
    print("part 2:", least_heat_loss(g2))
    print("--- %s seconds ---" % (time.time() - start2))
    