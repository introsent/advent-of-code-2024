blocks = []
count_non_dots = 0
dot_blocks_positions = []
with open('day_9/data.txt', 'r') as file:
    for line in file:
        for inx, char in enumerate(line.replace("\n", "")):
            if (inx % 2 == 0):
                ID = inx // 2
                for _ in range(int(char)):
                    blocks.append(str(ID))
                count_non_dots += int(char)
            else:
            
                dot_blocks_positions.append([len(blocks), len(blocks) + int(char) -1])
                for _ in range(int(char)):
                    blocks.append('.') 

dot_blocks_positions.pop()
print(blocks)
print(dot_blocks_positions)                    


cur_char = blocks[len(blocks) - 1]
cur_char_count = 0
for inx, char in enumerate(reversed(blocks)):
    print(inx)
    
    if cur_char != char:
        for inx_pos, pos in enumerate(dot_blocks_positions):
            if pos[1] - (pos[0]) + 1 >= cur_char_count and len(blocks) - inx >= pos[0]:
                for i in range(len(blocks) - inx, len(blocks) - inx + cur_char_count):
                    blocks[i] = '.'

                if (char != '.'):   
                    for i in range(pos[0], pos[0] + cur_char_count):
                        blocks[i] = cur_char        
                      
                    dot_blocks_positions[inx_pos][0] = pos[0] + cur_char_count 

                    if (dot_blocks_positions[inx_pos][0] > pos[1]):
                        dot_blocks_positions.pop(inx_pos) 
                    break     
                             
        if (char != '.'):                         
            cur_char_count = 0
            cur_char = char
    if (char != '.'): 
        cur_char_count += 1

print(blocks)  

sum = 0

for inx, char in enumerate(blocks):
    if char != '.':
        sum += int(char) * inx

print(sum)   



