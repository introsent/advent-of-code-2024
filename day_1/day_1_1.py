import bisect

rrow_list = []
lrow_list = []
sum = 0
with open('data.txt', 'r') as file:
    for line in file:
        rrow_value, lrow_value = map(int, line.split())
        bisect.insort(rrow_list, rrow_value)
        bisect.insort(lrow_list, lrow_value)

for r, l in zip(rrow_list , lrow_list):
    sum += abs(r - l)

print(sum)


