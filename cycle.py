# Python program for solution of 
# hamiltonian cycle problem 
import time
'''Backtrack'''

class Graph(): 
    def __init__(self, vertices): 
        self.graph = [[0 for column in range(vertices)]
                            for row in range(vertices)] 
        self.V = vertices 

    ''' Check if this vertex is an adjacent vertex 
        of the previously added vertex and is not 
        included in the path earlier '''
    def isSafe(self, v, pos, path): 
        # Check if current vertex and last vertex 
        # in path are adjacent 
        if self.graph[ path[pos-1] ][v] == 0: 
            return False

        # Check if current vertex not already in path 
        for vertex in path: 
            if vertex == v: 
                return False

        return True

    # A recursive utility function to solve 
    # hamiltonian cycle problem 
    def hamCycleUtil(self, path, pos): 

        # base case: if all vertices are 
        # included in the path 
        if pos == self.V: 
            # Last vertex must be adjacent to the 
            # first vertex in path to make a cycle 
            return True
            # if self.graph[ path[pos-1] ][ path[0] ] == 1: 
            #     return True
            # else: 
            #     return False
        
        # Try different vertices as a next candidate 
        # in Hamiltonian Cycle. We don't try for 0 as 
        # we included 0 as starting point in hamCycle() 
        for v in range(0,self.V): 

            if self.isSafe(v, pos, path) == True: 

                path[pos] = v 

                if self.hamCycleUtil(path, pos+1) == True: 
                    return True

                # Remove current vertex if it doesn't 
                # lead to a solution 
                path[pos] = -1

        return False

    def hamCycle(self): 
        path = [-1] * self.V 

        ''' Let us put vertex 0 as the first vertex 
            in the path. If there is a Hamiltonian Cycle, 
            then the path can be started from any point 
            of the cycle as the graph is undirected '''
        
        for i in range(self.V):
            path = [-1] * self.V 
            path[0] = i

            if self.hamCycleUtil(path,1) == True: 
                self.printSolution(path) 
                return True

        print("GA ADA")
        return False

    def printSolution(self, path): 
        print ("Solution Exists: Following",
                 "is one Hamiltonian Cycle")
        for vertex in path: 
            print (vertex, end = " ")
        # print (path[0], "\n")

# Driver Code 

# ''' Let us create the following graph 
#     (0)--(1)--(2) 
#     | / \ | 
#     | / \ | 
#     | /     \ | 
#     (3)-------(4) '''
# g1 = Graph(5) 
# g1.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1], 
#             [0, 1, 0, 0, 1,],[1, 1, 0, 0, 1], 
#             [0, 1, 1, 1, 0], ] 

# # Print the solution 
# g1.hamCycle(); 

# ''' Let us create the following graph 
#     (0)--(1)--(2) 
#     |    / \   | 
#     |   /   \  | 
#     | /      \ | 
#     (3)       (4) '''
# g2 = Graph(5) 
# g2.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1], 
#         [0, 1, 0, 0, 1,], [1, 1, 0, 0, 0], 
#         [0, 1, 1, 0, 0], ] 

# # Print the solution 
# g2.hamCycle(); 

# # This code is contributed by Divyanshu Mehta 
# g3 = Graph(3)
# g3.graph = [ [0,1,1],[1,0,0],[1,0,0] ]
# g3.hamCycle()

# g16 = Graph(16)
# g16.graph = [
#     [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
# ]
# start_time = time.time()
# g16.hamCycle()
# print("--- %s miliseconds ---" % ((time.time() - start_time)*1_000))

# g18 = Graph(18)
# g18.graph = [
#     [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
# ]

# start_time = time.time()
# g18.hamCycle()
# print("--- %s miliseconds ---" % ((time.time() - start_time)*1_000))


