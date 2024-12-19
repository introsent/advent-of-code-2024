patterns = []
count_available = 0

def is_design_possible(line, patterns, memo):
    if line in memo:  # Check if result is already cached
        return memo[line]
    
    if len(line) == 0:  # Base case: empty line is valid
        return True

    for pattern in patterns:
        if line.startswith(pattern):  # Faster substring check
            if is_design_possible(line[len(pattern):], patterns, memo):
                memo[line] = True  # Cache the result
                return True

    memo[line] = False  # Cache the result
    return False       

with open('day_19/data.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip()
        if i == 0:
            patterns = line.split(', ')
        elif line:
            memo = {}  # Initialize memoization dictionary
            if is_design_possible(line, patterns, memo):
                print(line)
                count_available += 1

print(count_available)