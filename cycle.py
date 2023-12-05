# Python program for solution of 
# hamiltonian Path problem 
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
    # hamiltonian Path problem 
    def hamPathUtil(self, path, pos): 

        # base case: if all vertices are 
        # included in the path 
        if pos == self.V: 
            # Last vertex must be adjacent to the 
            # first vertex in path to make a Path 
            return True
            # if self.graph[ path[pos-1] ][ path[0] ] == 1: 
            #     return True
            # else: 
            #     return False
        
        # Try different vertices as a next candidate 
        # in Hamiltonian Path. We don't try for 0 as 
        # we included 0 as starting point in hamPath() 
        for v in range(0,self.V): 

            if self.isSafe(v, pos, path) == True: 

                path[pos] = v 

                if self.hamPathUtil(path, pos+1) == True: 
                    return True

                # Remove current vertex if it doesn't 
                # lead to a solution 
                path[pos] = -1

        return False

    def hamPath(self): 
        path = [-1] * self.V 

        ''' Let us put vertex 0 as the first vertex 
            in the path. If there is a Hamiltonian Path, 
            then the path can be started from any point 
            of the Path as the graph is undirected '''
        
        for i in range(self.V):
            path = [-1] * self.V 
            path[0] = i

            if self.hamPathUtil(path,1) == True: 
                self.printSolution(path) 
                return True

        print("GA ADA")
        return False

    def printSolution(self, path): 
        print ("Solution Exists: Following",
                 "is one Hamiltonian Path")
        for vertex in path: 
            print (vertex, end = " ")