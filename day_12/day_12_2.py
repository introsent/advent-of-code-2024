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
    outer_perimeter = set()
    for value in block:
        x = value[0]
        y = value[1]

        top = (x-1, y) not in block
        bottom = (x+1, y) not in  block
        left = (x, y-1) not in block
        right = (x, y+1) not in block
    
        top_left = (x-1, y-1) not in block
        top_right = (x-1, y+1) not in block
        bottom_left = (x+1, y-1) not in block
        bottom_right = (x+1, y+1) not in block
        if top:
           outer_perimeter.add((x-1, y))
        if bottom: 
            outer_perimeter.add((x+1, y))
        if left: 
            outer_perimeter.add((x, y-1))
        if right: 
            outer_perimeter.add((x, y+1))    
        if top_right:  
            outer_perimeter.add((x-1, y+1)) 
        if top_left:
            outer_perimeter.add((x-1, y-1))
        if bottom_right:
            outer_perimeter.add((x+1, y+1))
        if bottom_left:
            outer_perimeter.add((x+1, y-1))            
    
    sides = 0
    print(outer_perimeter, " -> ",  block)
    for part in outer_perimeter:
        x = part[0]
        y = part[1]

        top = (x-1, y) in block
        bottom = (x+1, y) in block
        left = (x, y-1) in block
        right = (x, y+1) in block

        top_left = (x-1, y-1) in block
        top_right = (x-1, y+1) in block
        bottom_left = (x+1, y-1) in block
        bottom_right = (x+1, y+1) in block

        sum_top_left = int(top) + int(left) + int(top_left)
        if ( sum_top_left == 3 or ( sum_top_left == 1 and top_left == True) or ( sum_top_left == 2 and top_left == False) ):
            print(x, y)
            sides += 1

        sum_top_right = int(top) + int(right) + int(top_right) 
        if ( sum_top_right == 3 or ( sum_top_right == 1 and top_right == True) or ( sum_top_right == 2 and top_right == False)):
            print(x, y)
            sides += 1 

        sum_bottom_left = int(bottom) + int(left) + int(bottom_left)     
        if ( sum_bottom_left == 3 or (sum_bottom_left == 1 and bottom_left == True)  or (sum_bottom_left == 2 and bottom_left == False) ):
            print(x, y)
            sides += 1  

        sum_bottom_right = int(bottom) + int(right) + int(bottom_right)     
        if ( sum_bottom_right == 3 or (sum_bottom_right == 1 and bottom_right == True) or (sum_bottom_right == 2 and bottom_right == False)):
            print(x, y)
            sides += 1           

    print( sides)
    sum += len(block) * sides
        
print(sum)

