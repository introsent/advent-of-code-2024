chars_matrix = []
sum = 0
with open('day_4/data.txt', 'r') as file:
    for line in file:
        line_to_char_arr = [char for char in line.replace("\n", "")]

        chars_matrix.append(line_to_char_arr)
            
for x, xv in enumerate(chars_matrix):
    for y, yv in enumerate(xv):
        #horizontal
        if (y < len(xv) - 3):
            l = xv[y] + xv[y+1] + xv[y+2] + xv[y+3]
            if len(l) == len(set(l)):
                if (str(l) == "XMAS" or str(l) == "SAMX"):
                    sum+=1
        #vertical
        if (x < len(chars_matrix) - 3):
            l = chars_matrix[x][y] + chars_matrix[x+1][y] + chars_matrix[x+2][y] + chars_matrix[x+3][y]
            if len(l) == len(set(l)):
                if (str(l) == "XMAS" or str(l) == "SAMX"):
                    sum+=1 

        if (y < len(xv) - 3 and x < len(chars_matrix) - 3):
            l= chars_matrix[x][y] + chars_matrix[x+1][y+1] + chars_matrix[x+2][y+2] + chars_matrix[x+3][y+3]
            if len(l) == len(set(l)):
                if (str(l) == "XMAS" or str(l) == "SAMX"):
                    sum+=1

        if (y > 2 and x < len(chars_matrix) - 3):
            l = chars_matrix[x][y] + chars_matrix[x+1][y-1] + chars_matrix[x+2][y-2] + chars_matrix[x+3][y-3]
            if len(l) == len(set(l)):
                if (str(l) == "XMAS" or str(l) == "SAMX"):
                    sum+=1


print(sum)
