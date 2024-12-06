from collections import deque
 
def get_start(grid):
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "^":
                return i, j
    return None
 
 
adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]
 
grid = open("day_6/data.txt").read().splitlines()
sx, sy = get_start(grid)
 
visited = set([])
idx = 0
q = deque([(sx, sy, idx)])
while q:
    x, y, idx = q.popleft()
    dx, dy = adj[idx]
    visited.add((x, y))
   
    if not (0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0])):
        break
    
    if grid[x + dx][y + dy] == "#":
        
        idx = (idx + 1) % len(adj)
        q.append((x, y, idx))
    else:
        
        q.append((x + dx, y + dy, idx))
 
num_obstructions = 0
for i, j in visited:
    if i == sx and j == sy:
        continue
 
    visited = set([])
    idx = 0
    q = deque([(sx, sy, idx)])
    while q:
        x, y, idx = q.popleft()
        dx, dy = adj[idx]
        if (x, y, idx) in visited:
            num_obstructions += 1
            break
        visited.add((x, y, idx))
        if not (0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0])):
            break
        if grid[x + dx][y + dy] == "#" or (x + dx == i and y + dy == j):
            idx = (idx + 1) % len(adj)
            q.append((x, y, idx))
        else:
            q.append((x + dx, y + dy, idx))
 
print(num_obstructions)