import re

rows = 103
cols = 101
 
field = []
directions = []

start_pos = [0, 0]

with open('day_15/data.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.replace("\n", "")
        if line != "":
            if line[0] == '#':
                new_line = []
                for j, ch in enumerate(line):
                    if ch == '@':
                        start_pos[0] = i
                        start_pos[1] = j
                    new_line.append(ch)
                field.append(new_line)    
            else:  
                for ch in line:
                    directions.append(ch)  


for line in field:
    print(line)  

print()

right, left, top, bottom = [0, 1], [0, -1], [-1, 0], [1, 0]
pos = start_pos

cur_direction = []
for direction in directions:
    if direction == '^':
        cur_direction = top
    elif direction == '>':
        cur_direction = right
    elif direction == 'v':
        cur_direction = bottom
    elif direction == "<":
        cur_direction = left       


    block = []
    block.append(pos)

    desired_pos = pos
    dot_found = False

    while (desired_pos[0] >= 0 and desired_pos[0] < len(field)) and (desired_pos[1] >= 0 and desired_pos[1] < len(field[0])):
        desired_pos = [desired_pos[i] + cur_direction[i] for i in range(len(desired_pos))]
        
        if field[desired_pos[0]][desired_pos[1]] == '.':
            dot_found = True
            break
        elif field[desired_pos[0]][desired_pos[1]] == '#':
            dot_found = False
            break
        else:
            block.append(desired_pos)

    if dot_found:
        for position in reversed(block):
            next_position = [position[i] + cur_direction[i] for i in range(len(pos))]
            field[next_position[0]][next_position[1]] = field[position[0]][position[1]]

        field[pos[0]][pos[1]] = '.'
        pos = [pos[i] + cur_direction[i] for i in range(len(pos))]

for line in field:
    print(line)      

sum = 0
for i, line in enumerate(field):
    for j, ch in enumerate(line):
        if ch == "O":
            sum += 100 * i + j

print(sum)            

        


