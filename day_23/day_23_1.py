from collections import defaultdict


# Find triangles
def find_triangles(graph):
    triangles = []
    for node in graph:
        neighbors = graph[node]
        for neighbor1 in neighbors:
            for neighbor2 in neighbors:
                if neighbor1 != neighbor2 and neighbor2 in graph[neighbor1]:

                    triangles.append((node, neighbor1, neighbor2))
    # Remove duplicate triangles (e.g., (A, B, C) and (B, C, A))
    unique_triangles = set(tuple(sorted(triangle)) for triangle in triangles)
    return list(unique_triangles)

computer_graph = defaultdict(list) 

with open('day_23/data.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip()
        computers = line.split('-')
        computer_graph[computers[0]].append(computers[1])
        computer_graph[computers[1]].append(computers[0])

triangles = find_triangles(computer_graph)

count_t = 0
for triangle in triangles:
    for el in triangle:
        if el[0] == 't':
            count_t += 1
            break

print(triangles)
print(count_t)