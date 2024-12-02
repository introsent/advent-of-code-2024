
sum = 0
with open('day_2/data.txt', 'r') as file:
    for line in file:
        nums_in_line = line.split()
        nums_list = [int(s) for s in nums_in_line]

        is_increasing = all(i < j and abs(i - j) <= 3 for i, j in zip(nums_list, nums_list[1:]))
        is_decreasing = all(i > j and abs(i - j) <= 3 for i, j in zip(nums_list, nums_list[1:]))

        if (is_increasing or is_decreasing):
            sum += 1
                
        
print(sum)


