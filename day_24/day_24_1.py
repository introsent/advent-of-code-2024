from collections import defaultdict, OrderedDict

gates = defaultdict(list)

input_list = defaultdict(list)

def find_result(key, info):
    gate_info = info.split(' ')
    gate1 = gate_info[0]
    gate2 = gate_info[2]
    operator = gate_info[1] 

    if gate1 not in gates:
        find_result(gate1, input_list[gate1])
    
    if gate2 not in gates:
        find_result(gate2, input_list[gate2])

    if operator == "AND":
        if gates[gate1] == 1 and gates[gate2] == 1:
            gates[key] = 1
        else:
            gates[key] = 0
    elif operator == "OR":
        if gates[gate1] == 1 or gates[gate2] == 1:    
            gates[key] = 1
        else:
            gates[key] = 0      
    elif operator == "XOR":
        if gates[gate1] != gates[gate2]:
            gates[key] = 1
        else:
            gates[key] = 0     



is_empty_line_found = False
with open('data.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip()
        if line == '':
            is_empty_line_found = True
            continue

        if (not is_empty_line_found):
            start_gate = line.split(': ')
            gates[start_gate[0]] = int(start_gate[1])
        else:
            transition = line.split(' -> ')

            input_list[transition[1]] = transition[0]         


for gate_key in input_list:
    find_result(gate_key, input_list[gate_key])

sorted_dict = OrderedDict(sorted(gates.items()))

binary = ""   
for gate in reversed(sorted_dict):
    if gate[0] == 'z':
        binary += str(gates[gate])

print(binary)
print(int(binary, 2))        

