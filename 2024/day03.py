file_path = "inputs/input03.txt"
with open(file_path) as file:
    lines = []
    for line in file:
        lines.append(line)
full_memory = "".join(lines)

# Part 1
sum = 0
memory = full_memory
for _ in range(memory.count("mul(")):
    memory = memory.partition("mul(")[2]
    nums = memory.partition(")")[0].split(",")
    if len(nums) != 2:
        continue
    if not all(num.isnumeric() for num in nums):
        continue
    num1, num2 = nums
    sum += int(num1) * int(num2)
print("Part1:", sum)


# Part 2
sum = 0
memory = full_memory
for _ in range(memory.count("don't()")):
    before, _, after = memory.partition("don't()")
    after = after.partition("do()")[2]
    memory = before + after
for _ in range(memory.count("mul(")):
    memory = memory.partition("mul(")[2]
    nums = memory.partition(")")[0].split(",")
    if len(nums) != 2:
        continue
    if not all(num.isnumeric() for num in nums):
        continue
    num1, num2 = nums
    sum += int(num1) * int(num2)
print("Part2:", sum)


