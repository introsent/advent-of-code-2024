from collections import deque

#Not optimized enough 

rows = 71
cols = 71
maze = [['.'] * cols for _ in range( rows ) ]

cuts = []

with open('day_18/data.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.replace("\n", "")
        x, y = line.split(',')
        x, y = int(x), int(y)
        cuts.append([y, x])
        

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 

from collections import deque

def shortest_path(cuts_func, start, end):
    queue = deque([start])  # Start is (row, col)
    visited = set()
    visited.add(tuple(start))
    
    steps = 0  # Count the number of steps
    
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            
            if (x, y) == tuple(end):
                return steps
            
            # Explore all possible directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols and [ny, nx] not in cuts_func and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
        
        steps += 1  # Increment steps after exploring one level of the BFS
    
    return -1  # Return -1 if no valid path 

for i, cut in enumerate(cuts):
    if i > 1024:
        print(i)
        new_cut = cuts[0 : i + 1]
        if i > 1024 and shortest_path(new_cut, [0, 0], [rows-1, cols-1]) == -1:
            print(str(cut[1]) + ',' + str(cut[0]))  
            break      

        


