def read_file_to_list(file: str) -> list:
    output = open(file).read().split("\n")
    if not output[-1]:              # remove last line if it's blank
        output = output[0:-1]
    return output

def find_calibration_values(document: list) -> list:
    # finds the first and last digit in a line and combines it to make a 2 digit number
    calibration_values = []
    for line in document:

        for i in line:
            if i.isdigit():
                first_digit = i
                break

        for j in line[::-1]:
            if j.isdigit():
                last_digit = j
                break

        calibration_values.append(int(first_digit + last_digit))
    return calibration_values


def part2_find_calibration_values(document: list) -> list:
    calibration_values = []
    spelled_out_numbers = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9",
                           "1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9"}
    for line in document:
        first_digit_position = 99
        first_digit = ""
        last_digit_position = -1
        last_digit = ""
        for string in spelled_out_numbers:
            if -1 < line.find(string) < first_digit_position:
                first_digit_position = line.find(string)
                first_digit = spelled_out_numbers[string]

            if line.rfind(string) > last_digit_position:
                last_digit_position = line.rfind(string)
                last_digit = spelled_out_numbers[string]

        calibration_values.append(int(first_digit + last_digit))
    return calibration_values

            

    




if __name__ == "__main__":
    calibration_document = read_file_to_list("inputs/01/input.txt")
    calibration_values = find_calibration_values(calibration_document)
    print("part one:", sum(calibration_values))
    part2_calibration_values = part2_find_calibration_values(calibration_document)
    print("part two:", sum(part2_calibration_values))


    
