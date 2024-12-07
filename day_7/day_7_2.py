import itertools
signs = ['+', '*', '|']

sum = 0
with open('day_7/data.txt', 'r') as file:
    for line in file:
        line = line.replace("\n", "")

        total, numbers = line.split(":")

        total = int(total)
        nums_array = [int(num) for num in numbers.split()]

        possible_combinations = list(itertools.product(signs, repeat=(len(nums_array) - 1)))

        for combination in possible_combinations:
            ans = 0
            for inx, value in enumerate(nums_array):
                if inx == 0:
                    ans = value
                else: 
                    if combination[inx - 1] == '+':
                        ans += value
                    elif combination[inx - 1] == '*':
                        ans *= value
                    elif combination[inx - 1] == '|':
                        ans = int(str(ans) + str(value))
   

            if ans == total:
                sum += total
                break
                

print(sum)


     


