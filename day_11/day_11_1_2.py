from functools import cache


stones = []
with open('day_11/data.txt', 'r') as file:
    for line in file:
        stones = line.split()
        
@cache
def stones_counter(stone, iterations):
    print(iterations)
    if iterations == 0:
        return 1
    
    stone = str(int(stone))  

    if stone == '0':  
        return stones_counter('1', iterations - 1)
    
    elif len(stone) % 2 == 0:  
        mid = len(stone) // 2
        part1 = stone[:mid]
        part2 = stone[mid:]
        return stones_counter(part1, iterations - 1) + stones_counter(part2, iterations - 1)
    else:  
        return stones_counter(str(int(stone) * 2024) , iterations - 1)

count = 0
for stone in stones:
    count += stones_counter(stone, 75)

print(count)    

       

             

     