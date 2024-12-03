import re

file_in_one_line = ""

with open('day_3/data.txt', 'r') as file:
    for line in file:
        file_in_one_line += line

sum = 0

pattern_mul = r"mul\(\d+,\d+\)"
pattern_marker = r"(do\(\)|don't\(\))" 

inside_block = False 
matches = []

tokens = re.split(pattern_marker, file_in_one_line)
for token in tokens:
    if re.match(pattern_marker, token): 
        if "don't" in token:
            inside_block = True  
        elif "do" in token:
            inside_block = False  
    if not inside_block:
        mul_matches = re.findall(pattern_mul, token)
        if mul_matches:
            matches.extend(mul_matches)

for match in matches:
    numbers = re.findall(r"\d+", match)
    sum += int(numbers[0]) * int(numbers[1])     
        
print(sum)


