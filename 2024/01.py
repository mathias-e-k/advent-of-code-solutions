input_path = "inputs/01.txt"
with open(input_path) as input_file:
    list1 = []
    list2 = []
    for line in input_file:
        line = line.split("   ")
        list1.append(int(line[0]))
        list2.append(int(line[1]))

#list1 = [3, 4, 2, 1, 3, 3]
#list2 = [4, 3, 5, 3, 9, 3]

# Part 1
total_distance = 0
sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)
for i in range(len(list1)):
    total_distance += abs(sorted_list1[i] - sorted_list2[i])
print("part1:", total_distance)


# Part 2
counts = {key : list2.count(key) for key in set(list2)}
similarity_score = 0
for i in list1:
    if i not in counts:
        continue
    similarity_score += i * counts[i]
print("part2:", similarity_score)
