def fix_and_check_monotonic_once(sequence):
    def is_monotonic(seq):
        is_increasing = all(i < j and abs(i - j) <= 3 for i, j in zip(seq, seq[1:]))
        is_decreasing = all(i > j and abs(i - j) <= 3 for i, j in zip(seq, seq[1:]))

        return (is_increasing or is_decreasing)
   

    for i in range(len(sequence) - 1):
        if i > 0:
            if (sequence[i] >= sequence[i + 1] and sequence[i] >= sequence[i - 1]) or (sequence[i] <= sequence[i + 1] and sequence[i] <= sequence[i - 1]) or abs(sequence[i] - sequence[i + 1]) > 3 or abs(sequence[i] - sequence[i - 1]) > 3: 
                modified_sequence_1 = sequence[:i] + sequence[i + 1:]
                modified_sequence_2 = sequence[:i-1] + sequence[i:]
                modified_sequence_3 = sequence[:i+1] + sequence[i+2:]
                return  is_monotonic(modified_sequence_1) or is_monotonic(modified_sequence_2) or is_monotonic(modified_sequence_3)
            
    return is_monotonic(sequence)


sum = 0
with open('day_2/data.txt', 'r') as file:
    for line in file:
        nums_in_line = line.split()
        nums_list = [int(s) for s in nums_in_line]

        if (fix_and_check_monotonic_once(nums_list)):
            sum += 1                       
        
print(sum)


