from utils import read_file_to_list


def next_value(history: list) -> int:
    next_level = [history[1 + i] - history[i] for i in range(len(history) - 1)]
    if all(v == 0 for v in next_level):
        return history[-1]
    else:
        return history[-1] + next_value(next_level)


def previous_value(history: list) -> int:
    next_level = [history[1 + i] - history[i] for i in range(len(history) - 1)]
    if all(v == 0 for v in next_level):
        return history[0]
    else:
        return history[0] - previous_value(next_level)


if __name__ == "__main__":
    puzzle_input = read_file_to_list("inputs/09/input.txt")
    ecological_reading_histories = []
    for line in puzzle_input:
        ecological_reading_histories.append([int(i) for i in line.split()])
    

    sum_extrapolated_values = 0
    for reading_history in ecological_reading_histories:
        sum_extrapolated_values += next_value(reading_history)
    print(sum_extrapolated_values)

    #-------------------------------------------------------------------------

    sum_previous_values = 0
    for reading_history in ecological_reading_histories:
        sum_previous_values += previous_value(reading_history)
    print(sum_previous_values)
