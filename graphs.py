import random
from cycle import Graph
from path import Hamiltonian_path
import time
import resource

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
for i in range(len(vertices)):
    n = vertices[i]
    generated_graph = generate_graph(n)
    print(f"Generated Graph with {n} vertices:\n")
    #print_graph(generated_graph)
    n_graph = Graph(n)
    n_graph.graph = generated_graph

    '''Backtracking'''
    print('Backtracking: \n')
    start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    start_time = time.time()
    n_graph.hamPath()
    print()
    time_elapsed = time.time() - start_time
    end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    
    memory_used = (end_memory - start_memory) / 1024  # Convert to kilobytes
    print("Time elapsed: " + str(time_elapsed) + " miliseconds\n")
    print("Memory used: " + str(memory_used) + " KB\n")


    '''DP'''
    print('Dynamic Programming: \n')
    start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    start_time = time.time()
    result = Hamiltonian_path(generated_graph,n)
    time_elapsed = time.time() - start_time
    end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    memory_used = (end_memory - start_memory) / 1024  # Convert to kilobytes

    if (result):
        print("YES")
    else:
        print("NO")
    
    print("Time elapsed: " + str(time_elapsed) + " miliseconds")
    print("Memory used: " + str(memory_used) + " KB\n")
    print('\n-----------------')