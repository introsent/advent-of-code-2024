import re

rows = 103
cols = 101
field_positions = []
with open('day_14/data.txt', 'r') as file:
    for i, line in enumerate(file):
        numbers = re.findall(r"-?\d+\.\d+|-?\d+", line)
        field_positions.append(numbers)
    
smallest = 99999999
smallest_loop_count = 0
loop_count = 0
while (loop_count < rows * cols):
    q1, q2, q3, q4 = 0, 0, 0, 0
    field = [[0 for _ in range(cols)] for _ in range(rows)]
    for numbers in field_positions:
        x = int(numbers[0])
        y = int(numbers[1])
        numbers[0] = str( (x + int(numbers[2])) % cols)
        numbers[1] = str( (y + int(numbers[3])) % rows)

        if y < rows// 2 and x < cols // 2:
            q1 += 1
        elif y < rows // 2 and x > cols // 2:
            q2 += 1
        elif y > rows // 2 and x < cols // 2:
            q3 += 1
        elif y > rows // 2 and x > cols // 2:
            q4 += 1
        
    distribution = q1 * q2 * q3 * q4
    if (distribution < smallest) :
        smallest = distribution   
        smallest_loop_count = loop_count             

    loop_count += 1
print(smallest_loop_count) 

field = [['.' for _ in range(cols)] for _ in range(rows)]
with open('day_14/data.txt', 'r') as file:
    for i, line in enumerate(file):
        numbers = re.findall(r"-?\d+\.\d+|-?\d+", line)
        x = int(numbers[0])
        y = int(numbers[1])
        loop_count = 0
        while (loop_count < smallest_loop_count):
            x += int(numbers[2])
            y += int(numbers[3])
            loop_count += 1

        x = x % cols
        y = y % rows

        field[y][x] = '*'

out = open("day_14/out.txt", "w")

out.write(str(smallest_loop_count))
out.write("\n")
for line in field:
    out_line = ""
    for char in line:
        out_line += char
    out.write(out_line)
    out.write("\n")
out.close()  


