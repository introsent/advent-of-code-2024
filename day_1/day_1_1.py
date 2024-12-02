import bisect

rrow_list = []
lrow_list = []
sum = 0
with open('day_1/data.txt', 'r') as file:
    for line in file:
        lrow_value, rrow_value = map(int, line.split())
        bisect.insort(lrow_list, lrow_value)
        bisect.insort(rrow_list, rrow_value)

for r, l in zip(rrow_list , lrow_list):
    sum += abs(r - l)

print(sum)


