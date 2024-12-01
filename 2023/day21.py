class Graph:
    def __init__(self, puzzle_input) -> None:
        self.puzzle_map = puzzle_input
        self.map_height = len(self.puzzle_map)
        self.map_width = len(self.puzzle_map[0])
        self.start_pos = (0, 0)
        for y, line in enumerate(self.puzzle_map):
            if "S" in line:
                x = line.find("S")
                self.start_pos = (y, x)
                break
        else:
            raise AttributeError("start not found")
    
    def get_start(self):
        return self.start_pos

    def neighbours(self, node):
        output = []
        y, x = node
        up = (y - 1, x)
        down = (y + 1, x)
        left = (y, x - 1)
        right = (y, x + 1)
        for direction in (up, down, left, right):
            y, x = direction
            y = y % self.map_height
            x = x % self.map_width
            if self.puzzle_map[y][x] == "#":
                continue
            output.append(direction)
        return output


def reachable_plots(graph, steps):
    even_odd_parity = [1, 0]
    step = 0
    start = graph.get_start()
    reached_plots = set()
    next_frontier = [start]
    reached_plots.add(start)
    while step < steps:
        step += 1
        frontier = next_frontier.copy()

        for current in frontier:
            for next in graph.neighbours(current):
                if next not in reached_plots:
                    next_frontier.append(next)
                    reached_plots.add(next)
                    even_odd_parity[step % 2] += 1
    return even_odd_parity[steps % 2]

    

def make_quadratic_function(nums: list):
    '''Takes in numbers from a quadratic function, and returns that function.
    The numbers have to be [f(0), f(1), f(2)] for this function to work'''
    d1 = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    d2 = [d1[i+1] - d1[i] for i in range(len(d1)-1)]
    a = d2[0] // 2
    b = d1[0] - a
    c = nums[0]
    return lambda x: a*x**2 + b*x + c


def part2(puzzle_input, steps):
    # coded this after seeing this post: https://www.reddit.com/r/adventofcode/comments/18orn0s/2023_day_21_part_2_links_between_days/ 

    # Originally i tried to code a geometric solution but i missed a few important details, so it didn't work
    # Geometric solution would be much faster, since you would only 
    # have to count a few thousand plots instead of almost 150 000 plots 
    # geometric solution: https://www.reddit.com/r/adventofcode/comments/18nol3m/2023_day_21_a_geometric_solutionexplanation_for/ 

    STEPS_TO_EDGE = steps % len(puzzle_input)   # 65
    BIG_STEP = len(puzzle_input)                # 131
    NUMBER_OF_BIG_STEPS = steps // BIG_STEP     # 202300
    garden_plots_list = []
    for i in range(3):
        garden_plots_list.append(reachable_plots(puzzle_input_graph, STEPS_TO_EDGE + BIG_STEP*i))
    POLYNOMIAL = make_quadratic_function(garden_plots_list)

    return POLYNOMIAL(NUMBER_OF_BIG_STEPS)


if __name__ == "__main__":
    file = "inputs/21/input.txt"
    puzzle_input = open(file).read().strip().split("\n")
    puzzle_input_graph = Graph(puzzle_input)


    print("part 1:", reachable_plots(puzzle_input_graph, 64))
    print("part 2:", part2(puzzle_input, 26501365))