from functools import lru_cache

def find_all_designs(line, patterns):
    @lru_cache(None)
    def dp(i):
        if i == len(line):
            return 1  
        total_designs = 0
        for pattern in patterns:
            if i + len(pattern) <= len(line) and line[i:i + len(pattern)] == pattern:
                total_designs += dp(i + len(pattern))
        return total_designs

    return dp(0)

patterns = []
count_available = 0

with open('day_19/data.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip()
        if i == 0:
            patterns = line.split(', ')
        elif line:
            count_available += find_all_designs(line, patterns)

print(f"Count of valid lines: {count_available}")
