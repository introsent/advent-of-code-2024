from collections import deque

rows = 71
cols = 71
maze = [['.'] * cols for _ in range( rows ) ]

print(maze)
with open('day_18/data.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.replace("\n", "")
        x, y = line.split(',')
        x, y = int(x), int(y)
        maze[y][x] = '#'
        
            
print(maze)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 

from collections import deque

def shortest_path(maze, start, end):
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
                
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#' and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
        
        steps += 1  # Increment steps after exploring one level of the BFS
    
    return -1  # Return -1 if no valid path 

print(shortest_path(maze, [0, 0], [rows-1, cols-1]))          

        


