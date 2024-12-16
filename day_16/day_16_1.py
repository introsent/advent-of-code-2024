from collections import deque

maze = []

start_pos = ()
end_pos = ()
with open('day_16/data.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.replace("\n", "")
        new_line = []
        for j, ch in enumerate(line):
            if ch == 'S':
                start_pos = (i, j)
            if ch == 'E':
                end_pos = (i, j)
            new_line.append(ch)
        maze.append(new_line)    
            
print(start_pos, end_pos)

rows, cols = len(maze), len(maze[0])
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 


import heapq

def min_reindeer_score(maze, start, end):

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
   
    rows, cols = len(maze), len(maze[0])

    pq = []
    heapq.heappush(pq, (0, start[0], start[1], 0))  
    
    visited = set()
    visited.add((start[0], start[1], 0))

    while pq:
        score, x, y, dir_index = heapq.heappop(pq)

        if (x, y) == end:
            return score

        # 1. Move Forward
        dx, dy = directions[dir_index]
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
            if (nx, ny, dir_index) not in visited:
                heapq.heappush(pq, (score + 1, nx, ny, dir_index))
                visited.add((nx, ny, dir_index))

        # 2. Rotate Clockwise (90°)
        new_dir_index_cw = (dir_index + 1) % 4
        if (x, y, new_dir_index_cw) not in visited:
            heapq.heappush(pq, (score + 1000, x, y, new_dir_index_cw))
            visited.add((x, y, new_dir_index_cw))

        # 3. Rotate Counterclockwise (90°)
        new_dir_index_ccw = (dir_index - 1) % 4
        if (x, y, new_dir_index_ccw) not in visited:
            heapq.heappush(pq, (score + 1000, x, y, new_dir_index_ccw))
            visited.add((x, y, new_dir_index_ccw))

    return -1  # If there's no valid path

print(min_reindeer_score(maze, start_pos, end_pos))          

        


