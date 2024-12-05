chars_matrix = []
sum = 0
with open('day_4/data.txt', 'r') as file:
    for line in file:
        line_to_char_arr = [char for char in line.replace("\n", "")]
        chars_matrix.append(line_to_char_arr)
            
for x, xv in enumerate(chars_matrix):
    for y, yv in enumerate(xv):
        if (y < len(xv) - 2 and x < len(chars_matrix) - 2):
            l1 = chars_matrix[x][y] + chars_matrix[x+1][y+1] + chars_matrix[x+2][y+2]
            l2 = chars_matrix[x][y+2] + chars_matrix[x+1][y+1] + chars_matrix[x+2][y]
            if ((str(l1) == "MAS" or str(l1) == "SAM") and (str(l2) == "MAS" or str(l2) == "SAM")):
                sum+=1

print(sum)
