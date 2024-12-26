keys = []
locks = []

block_height = 8

is_lock = True

block = [0, 0, 0, 0, 0]

with open('day_25/data.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip()

        if i % block_height == 0:
            if line[0] == '#':
                is_lock = True
            elif line[0] == '.':
                is_lock = False
        else:
            if i % block_height < 6:
                for j, el in enumerate(line):
                    if el == '#':
                        block[j] += 1
            elif i % block_height == 6 :
                if is_lock:
                    locks.append(block)
                else:
                    keys.append(block)
                block = [0, 0, 0, 0, 0]                    
            
print(locks)
print(keys)            
   

count = 0
for key in keys:
    for lock in locks:
        fit = True
        for i, _ in enumerate(key):
            if key[i] + lock[i] > 5:
                fit = False
        if fit:
            count += 1

print(count)

