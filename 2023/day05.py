class range_map:
    def __init__(self, map_str: list) -> None:
        map_list = map_str.split("\n")
        self.name = map_list[0]
        self.ranges = []
        self.process_ranges(map_list[1:])

    def process_ranges(self, ranges):
        for line in ranges:
            line = line.split()
            range_start = int(line[1])
            range_end = range_start + int(line[2]) - 1
            change = int(line[0]) - range_start
            self.ranges.append([range_start, range_end, change])
        self.ranges.sort()

    def convert_number(self, num):
        for r in self.ranges:
            if self.in_range(num, r):
                return num + r[2]
        return num
    
    def in_range(self, num, r):
        if r[0] <= num <= r[1]:
            return True
        else: 
            return False

    def convert_ranges(self, num_ranges) -> list:
        output = []
        for num_range in num_ranges:
            num_start = num_range[0]
            num_end = num_range[1]
            reached_end = False

            for r in self.ranges:
                if num_start > r[1]:
                    continue
                    
                if num_start < r[0] and num_end >= r[0]:    # might be unneeded
                    output.append([num_start, r[0]-1])
                    num_start = r[0]

                if num_start >= r[0] and num_end >= r[1]:
                    output.append([num_start+r[2], r[1]+r[2]])
                    num_start = r[1] + 1
                
                if num_start >= r[0] and num_end <= r[1]:
                    output.append([num_start+r[2], num_end+r[2]])
                    reached_end = True

            if not reached_end:
                output.append([num_start, num_end])
        return output




if __name__ == "__main__":
    puzzle_input = open("inputs/05/input.txt").read().strip().split("\n\n")
    seed_numbers = puzzle_input[0].split(" ")[1:]
    x_to_y_maps = [range_map(puzzle_input[i+1]) for i in range(len(puzzle_input)-1)]
    numbers = [int(x) for x in seed_numbers]
    for map in x_to_y_maps:
        numbers = [map.convert_number(i) for i in numbers]
    print("part 1:", min(numbers))

#----------------------------------------------------------------------------------------

    numbers = [int(x) for x in seed_numbers]
    number_ranges = []

    for i in range(len(numbers) // 2):
        range_start = numbers[0 + i*2]
        range_end = range_start + numbers[1 + i*2] -1
        number_ranges.append([range_start, range_end])

    for map in x_to_y_maps:
        number_ranges = map.convert_ranges(number_ranges)

    number_ranges.sort()
    print("part 2:", number_ranges[0][0])
