chars_matrix = []
sum = 0
letter_positions = {}
with open('day_8/data.txt', 'r') as file:
    for row, line in enumerate(file):
        line_char = []
        for col, char in enumerate(line.replace("\n", "")):
            line_char.append(char)
            if char != '.':
                pos = [row, col]
                letter_positions.setdefault(char, []).append(pos)
        chars_matrix.append(line_char)        

grid = [['.' for _ in range(len(chars_matrix))] for _ in range(len(chars_matrix[0]))]

import itertools
 
for key in letter_positions:
    values = letter_positions[key]
    possible_combinations = list(itertools.combinations(values, 2))
    for positions in possible_combinations:
        first = positions[0]
        second = positions[1]

        row_offset = first[0] - second[0]
        col_offset = first[1] - second[1]

        row_first = first[0] + row_offset 
        col_first = first[1] + col_offset

        if (row_first in range(0, len(chars_matrix)) and col_first in range(0, len(chars_matrix[0]))):
            if (grid[row_first][col_first] == '.'):
                grid[row_first][col_first] = '#'
                sum += 1

        row_second = second[0] - row_offset 
        col_second = second[1] - col_offset
        if (row_second in range(0, len(chars_matrix)) and col_second in range(0, len(chars_matrix[0]))):
            if (grid[row_second][col_second] == '.'):
                grid[row_second][col_second] = '#'
                sum += 1
           
print(sum)
