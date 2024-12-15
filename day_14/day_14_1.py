import re

rows = 103
cols = 101
 
field = [[0 for _ in range(cols)] for _ in range(rows)]

with open('day_14/data.txt', 'r') as file:
    for i, line in enumerate(file):
        numbers = re.findall(r"-?\d+\.\d+|-?\d+", line)
        x = int(numbers[0])
        y = int(numbers[1])
        loop_count = 0
        while (loop_count < 100):
            x += int(numbers[2])
            y += int(numbers[3])
            loop_count += 1

        x = x % cols
        y = y % rows

        field[y][x] += 1
  
q1, q2, q3, q4 = 0, 0, 0, 0
for i, line in enumerate(field):
    for j, value in enumerate(line):
        if i < len(field) // 2 and j < len(line) // 2:
            q1 += value
        elif i < len(field) // 2 and j > len(line) // 2:
            q2 += value
        elif i > len(field) // 2 and j < len(line) // 2:
            q3 += value
        elif i > len(field) // 2 and j > len(line) // 2:
            q4 += value    

        

sum = q1 * q2 * q3 * q4
 
        
print(sum)

