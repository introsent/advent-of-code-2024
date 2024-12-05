import sys

def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
  
    rules = []
    updates = []
    is_rules = True

    for line in lines:
        trimmed = line.strip()

        if not trimmed:
            is_rules = False
            continue

        if is_rules:
            if '|' in trimmed:
                x, y = map(int, trimmed.split('|'))
                rules.append((x, y))
        else:
            updates.append(list(map(int, trimmed.split(','))))

    return rules, updates

def find_middle_page(update):
    if not update:
        return 0
    return update[len(update) // 2]

def main(filename):
    # Parsing the input
    rules, updates = parse_input(filename)
    
    valid_sum = 0
    fixed_sum = 0
    
    for update in updates:
        positions = {page: idx for idx, page in enumerate(update)}
        is_valid = True
        for x, y in rules:
            if x in positions and y in positions:
                if positions[x] > positions[y]:
                    is_valid = False
                    break
        
        middle_page = find_middle_page(update)
        
        if is_valid:
            valid_sum += middle_page
        else:
            graph = {page: [] for page in update}
            in_degree = {page: 0 for page in update}
            
            for x, y in rules:
                if x in positions and y in positions:
                    graph[x].append(y)
                    in_degree[y] += 1
            
            queue = [node for node, deg in in_degree.items() if deg == 0]
            result = []
            while queue:
                current = queue.pop(0)
                result.append(current)
                for neighbor in graph[current]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            if len(result) == len(update):
                fixed_sum += find_middle_page(result)
            else:
                fixed_sum += middle_page  

    print(f"Part 1 sum: {valid_sum}")
    print(f"Part 2 sum: {fixed_sum}")

if __name__ == '__main__':
    input_file = "day_5/data.txt"
    main(input_file)
   
