import random
from Path import Graph
from path import Hamiltonian_path
import time
import gc

def backtracking_analysis(n, generated_graph):
    print('Backtracking: \n')

    # Enable garbage collector
    gc.enable()

    # Measure start time
    start_time = time.time()

    # Measure start memory
    start_memory = gc.mem_alloc()

    n_graph = Graph(n)
    n_graph.graph = generated_graph
    n_graph.hamPath()

    # Force garbage collection and measure end memory
    gc.collect()
    end_memory = gc.mem_alloc()

    # Measure end time
    end_time = time.time()

    time_elapsed = end_time - start_time
    memory_used = (end_memory - start_memory) / 1024  # Convert to kilobytes
    print("Time elapsed: " + str(time_elapsed) + " seconds")
    print("Memory used: " + str(memory_used) + " KB\n")

def dp_analysis(n, generated_graph):
    print('Dynamic Programming: \n')

    # Enable garbage collector
    gc.enable()

    # Measure start time
    start_time = time.time()

    # Measure start memory
    start_memory = gc.mem_alloc()

    result = Hamiltonian_path(generated_graph, n)

    # Force garbage collection and measure end memory
    gc.collect()
    end_memory = gc.mem_alloc()

    # Measure end time
    end_time = time.time()

    time_elapsed = end_time - start_time
    memory_used = (end_memory - start_memory) / 1024  # Convert to kilobytes

    if result:
        print("YES")
    else:
        print("NO")
    
    print("Time elapsed: " + str(time_elapsed) + " seconds")
    print("Memory used: " + str(memory_used) + " KB\n")

def generate_graph(n, probability=0.3):
    if n < 2:
        raise ValueError("Number of vertices should be at least 2")

    graph = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < probability:
                graph[i][j] = 1
                graph[j][i] = 1

    return graph

# Generating graphs with 16, 18, and 20 vertices
vertices = [16, 18, 20]
for n in vertices:
    generated_graph = generate_graph(n)
    print(f"Generated Graph with {n} vertices:\n")
    
    backtracking_analysis(n, generated_graph)
    print('\n-----------------\n')
    
    dp_analysis(n, generated_graph)
    print('\n-----------------\n')
