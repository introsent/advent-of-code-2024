blocks = []
count_non_dots = 0

iterations_count = 0
with open('day_9/data.txt', 'r') as file:
    for line in file:
        iterations_count += 1
        for inx, char in enumerate(line.replace("\n", "")):
            if (inx % 2 == 0):
                ID = inx // 2
                for _ in range(int(char)):
                    blocks.append(str(ID))
                count_non_dots += int(char)
            else:
                for _ in range(int(char)):
                    blocks.append('.') 


moved_blocks = []
for inx, char in enumerate(blocks):
    if (len(moved_blocks) == count_non_dots):
        break

    if char == '.':
        pop_inx = 0
        for r_inx, r_char in enumerate(reversed(blocks)):
            if r_char != '.':
                pop_inx = r_inx
                break
        moved_blocks.append(blocks[len(blocks) - pop_inx - 1])
        blocks = blocks[:( - pop_inx -1)]
    else:
        moved_blocks.append(char)    

sum = 0

for inx, char in enumerate(moved_blocks):
    sum += int(char) * inx

print(sum)   



