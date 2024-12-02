lrow_list = []
rrow_list = []
sum = 0
with open('day_1/data.txt', 'r') as file:
    for line in file:
        lrow_value, rrow_value = map(int, line.split())
        lrow_list.append(lrow_value)
        rrow_list.append(rrow_value)

sum = 0
for l in lrow_list:
    sum += l * rrow_list.count(l)

print (sum)