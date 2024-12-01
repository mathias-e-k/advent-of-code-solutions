def read_file_to_list(file: str) -> list:
    return open(file).read().strip().split("\n")

def read_file_to_list_double_nl(file: str) -> list:
    return open(file).read().strip().split("\n\n")

from queue import PriorityQueue

def A_star(graph):
    # modified A* algorithm
    # only difference is i don't keep paths
    # https://www.redblobgames.com/pathfinding/a-star/introduction.html#more 

    todo = PriorityQueue()
    start = ()
    todo.put((0, start))
    cost = dict()
    cost[()] = 0 
    
    while todo:
        current = todo.get()[1]

        if current[1] == graph.goal:
            print(len(cost))
            return current[0]
        
        for next in graph.neighbours(current):
            next_cost = next[0]
            if next not in cost or next_cost < cost[next]:
                cost[next] = next_cost
                priority = next_cost + (graph.goal[0] - next[1][0] + graph.goal[1] - next[1][1])*1
                todo.put((priority, next))


if __name__ == "__main__":
    file = "inputs/21/input.txt"
    puzzle_input = open(file).read().strip().split("\n")
    for l in puzzle_input:
        print(l)