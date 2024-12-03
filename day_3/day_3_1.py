import re

sum = 0
pattern = r"mul\(\d+,\d+\)"

with open('day_3/data.txt', 'r') as file:
    for line in file:
        for match in re.findall(pattern, line):
            numbers = re.findall(r"\d+", match)
            sum += int(numbers[0]) * int(numbers[1])
             
print(sum)


