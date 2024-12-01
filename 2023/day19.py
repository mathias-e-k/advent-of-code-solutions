def get_accepted_parts(parts, workflows) -> list:
    output = []
    for part in parts:
        
        current_workflow = "in"
        while current_workflow not in "RA":
            workflow = workflows[current_workflow]

            for i in range(len(workflow) - 1):
                rule, next_workflow = workflow[i].split(":")
                category = rule[0]
                operator = rule[1]
                value = int(rule[2 :])
                if operator == ">" and part[category] > value:
                    current_workflow = next_workflow
                    break
                elif operator == "<" and part[category] < value:
                    current_workflow = next_workflow
                    break
            else:
                current_workflow = workflow[-1]
        
        if current_workflow == "A": output.append(part)
        elif current_workflow == "R": continue
        else: raise ValueError
    return output


def distinct_accepted_ratings(ranges: dict, next: str) -> int:
    output = 0

    if next == "A":
        x = ranges["x"]
        m = ranges["m"]
        a = ranges["a"]
        s = ranges["s"]
        return (1 + x[1] - x[0]) * (1 + m[1] - m[0]) * (1 + a[1] - a[0]) * (1 + s[1] - s[0])
    elif next == "R":
        return 0
    
    workflow = workflows[next]
    
    ranges = ranges.copy()
    for i in range(len(workflow) - 1):
        rule, next_workflow = workflow[i].split(":")
        category = rule[0]
        operator = rule[1]
        value = int(rule[2 :])

        if operator == ">" and ranges[category][1] > value:
            new_min = value + 1
            new_max = ranges[category][1]
            new_ranges = ranges.copy()
            new_ranges[category] = [new_min, new_max]
            output += distinct_accepted_ratings(new_ranges, next_workflow)
            ranges[category] = [ranges[category][0], value]

        elif operator == "<" and ranges[category][0] < value:
            new_min = ranges[category][0]
            new_max = value - 1
            new_ranges = ranges.copy()
            new_ranges[category] = [new_min, new_max]
            output += distinct_accepted_ratings(new_ranges, next_workflow)
            ranges[category] = [value, ranges[category][1]]

    output += distinct_accepted_ratings(ranges, workflow[-1])

    return output

        

if __name__ == "__main__":
    file = "inputs/19/input.txt"
    workflows_str, parts_str = open(file).read().strip().split("\n\n")
    workflows_str = workflows_str.split("\n")
    parts_str = [part[1 : -1] for part in parts_str.split("\n")]

    workflows = {}
    for workflow in workflows_str:
        workflows[workflow.partition("{")[0]] = workflow.partition("{")[2][: -1].split(",")

    parts = []
    for part in parts_str:
        p = {}
        for category in part.split(","):
            p[category.partition("=")[0]] = int(category.partition("=")[2])
        parts.append(p)
    accepted_parts = get_accepted_parts(parts, workflows)
    total = 0
    for part in accepted_parts:
        total += part["x"]
        total += part["m"]
        total += part["a"]
        total += part["s"]
    print("Part 1", total)

    #--------------------------------------------------------------------------
    
    ranges = {"x" : [1, 4000], "m" : [1, 4000], "a" : [1, 4000], "s" : [1, 4000]}
    total_ratings = distinct_accepted_ratings(ranges, "in")
    print("Part 2", total_ratings)