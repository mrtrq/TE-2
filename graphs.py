import random
from cycle import Graph
from path import Hamiltonian_path
import time

def generate_graph(n, probability=0.3):
    if n < 2:
        raise ValueError("Number of vertices should be at least 2")

    graph = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < probability:
                # Connect vertices with probability
                graph[i][j] = 1
                graph[j][i] = 1

    return graph

def print_graph(graph):
    for row in graph:
        print(row)

# Generating graphs with 16,18, and 20 vertices
vertices = [16,18,20]
for i in range(3):
    n = vertices[i]
    generated_graph = generate_graph(n)
    print(f"Generated Graph with {n} vertices:\n")
    #print_graph(generated_graph)
    n_graph = Graph(n)
    n_graph.graph = generated_graph

    print('Backtracking: \n')
    start_time = time.time()
    n_graph.hamCycle()
    print()
    time_elapsed = time.time() - start_time
    print("Time elapsed: " + str(time_elapsed) + " miliseconds\n")



    print('Dynamic Programming: \n')
    start_time = time.time()
    result = Hamiltonian_path(generated_graph,n)
    time_elapsed = time.time() - start_time
    if (result):
        print("YES")
    else:
        print("NO")
    
    print("Time elapsed: " + str(time_elapsed) + " miliseconds")
    print('\n-----------------')

    # g16 = Graph(16)
    # g16.graph = generated_graph
    # g16.hamCycle()
