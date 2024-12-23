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

def bron_kerbosch(R, P, X, graph, cliques):
    if not P and not X:
        cliques.append(R)
        return
    for node in list(P):
        neighbors = set(graph[node])
        bron_kerbosch(R.union({node}), P.intersection(neighbors), X.intersection(neighbors), graph, cliques)
        P.remove(node)
        X.add(node)

def find_maximal_cliques(graph):
    nodes = set(graph.keys())
    cliques = []
    bron_kerbosch(set(), nodes, set(), graph, cliques)
    return cliques

computer_graph = defaultdict(list) 

with open('day_23/data.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip()
        computers = line.split('-')
        computer_graph[computers[0]].append(computers[1])
        computer_graph[computers[1]].append(computers[0])


maximal_cliques = find_maximal_cliques(computer_graph)

sorted_cliques = [sorted(list(clique)) for clique in maximal_cliques]
sorted_cliques.sort()

largest_clique = max(sorted_cliques, key=len)

for inx, computer in enumerate(largest_clique):
    if inx < len(largest_clique) - 1:
        print(computer, end=",")
    else:
        print(computer, end="")    
    
