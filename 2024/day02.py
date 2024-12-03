file_path = "inputs/input02.txt"
with open(file_path) as file:
    reports = []
    for line in file:
        reports.append([int(i) for i in line.split()])

# Part 1
def is_safe(report: list):
    differences = [report[i+1] - report[i] for i in range(len(report)-1)]
    if not (all(i > 0 for i in differences) or all(i < 0 for i in differences)):
        return False
    if any(abs(i) > 3 for i in differences):
        return False
    return True

safe_reports = 0
for report in reports:
    if is_safe(report):
        safe_reports += 1
print("Part1:", safe_reports)

# Part 2
safe_reports = 0
for report in reports:
    for removed_level in range(len(report)):
        if is_safe(report[:removed_level] + report[removed_level+1:]):
            safe_reports += 1
            break
print("Part2:", safe_reports)
