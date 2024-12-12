def find_blocks(grid, target_char):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and not visited[x][y] and grid[x][y] == target_char

    def dfs(x, y, block):
        visited[x][y] = True
        block.append((x, y)) 

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                dfs(nx, ny, block)

    blocks = []

    for i in range(rows):
        for j in range(cols):
            if is_valid(i, j):
                current_block = []
                dfs(i, j, current_block)
                blocks.append(current_block) 

    return blocks

set_chars = set()
chars = []
with open('day_12/data.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip()
        nline = []
        for j, char in enumerate(line.strip()):
            set_chars.add(char)
            nline.append(char)
        chars.append(line)    
            
blocks = []
for char in set_chars:
    blocks += find_blocks(chars, char)

sum = 0
for block in blocks:
    perimeter = 0
    for value in block:
      
        x = value[0]
        y = value[1]

        top = (x-1, y) not in block
        bottom = (x+1, y) not in  block
        left = (x, y-1) not in block
        right = (x, y+1) not in block
    
        if top:
            perimeter += 1
        if bottom: 
            perimeter += 1
        if left: 
            perimeter += 1
        if right: 
            perimeter += 1       
    
    sum += len(block) * perimeter
        
print(sum)

