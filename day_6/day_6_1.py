map = []
start_pos_guard_x = 0
start_pos_guard_y = 0

with open('day_6/test_data.txt', 'r') as file:
    for inx_y, line in enumerate(file):
        line_to_char_arr = []
        for inx_x, char in enumerate(line.replace("\n", "")):
            if char == "^":
                start_pos_guard_x = inx_x;
                start_pos_guard_y = inx_y;
            
            line_to_char_arr.append(char)
        map.append(line_to_char_arr)


from enum import Enum
direction = {
    "up" : [-1, 0],
    "right" : [0, 1],
    "down" : [1, 0],
    "left" : [0, -1]   
}
     

current_direction_str = "up"
current_direction = direction[current_direction_str];
current_pos_x = start_pos_guard_x
current_pos_y = start_pos_guard_y

desired_pos_x = start_pos_guard_x
desired_pos_y = start_pos_guard_y + current_direction[0]

visited_pos_count = 0

while (desired_pos_x >= 0 and desired_pos_x < len(map[0])) and (desired_pos_y >= 0 and desired_pos_y < len(map)):
    if map[desired_pos_y][desired_pos_x] == "#":
        match current_direction_str:
            case "up":
                current_direction_str = "right"
            case "right":
                current_direction_str = "down"
            case "down":
                current_direction_str = "left"
            case "left": 
                current_direction_str = "up"
        current_direction = direction[current_direction_str]

    else:
        current_pos_x = desired_pos_x
        current_pos_y = desired_pos_y
        if (map[desired_pos_y][desired_pos_x] != "X"):
            map[desired_pos_y][desired_pos_x] = "X"
            visited_pos_count += 1
                          

    desired_pos_x = current_pos_x + current_direction[1]       
    desired_pos_y = current_pos_y + current_direction[0]   
    

for line in map:
    print(line)         
print(visited_pos_count)
