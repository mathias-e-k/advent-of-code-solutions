from utils import read_file_to_list


def hash_algorithm(_str : str):
    current_value = 0
    for c in _str:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


def hash_algorithm_label(_str : str):
    current_value = 0
    for c in _str:
        if c in ["=", "-"]:
            break
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


def focusing_power(boxes: list) -> int:
    total = 0
    for i, box in enumerate(boxes, start=1):
        for j, focal_length in enumerate(box.values(), start=1):
            total += i * j * focal_length
    return total

if __name__ == "__main__":
    puzzle_input = read_file_to_list("inputs/15/input.txt")[0]
    puzzle_input = puzzle_input.split(",")
    total = 0
    for s in puzzle_input:
        total += hash_algorithm(s)
    print("part 1:", total)

    #------------------------------------------------------------------------
    
    boxes = []
    for i in range(256):
        boxes.append({})

    for step in puzzle_input:
        for i, c in enumerate(step):
            if not c.isalpha():
                operation = c
                label = step[: i]
                box_num = hash_algorithm_label(label)
                break

        if operation == "=":
            focal_length = step[-1]
            boxes[box_num].update({label : int(focal_length)})
        elif operation == "-":
            boxes[box_num].pop(label, None)

    print("part 2:", focusing_power(boxes))

