"""Implementation of a Graph ADT

Author: Daniel Mitchell
Student Number: 20239030
Last edited: 04-4-2022
"""

import random

# Vertex class used for graph implementation 
class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight

# Graph implementation 
class Graph:
    # Initializes a Graph instance 
    def __init__(self, numvert):
        self.vertices = {}

        # Create dictionary of the graphs vertexes 
        for i in range(numvert):
            vertex = Vertex(i+1)
            self.add_vertex(vertex)

        # Create a random connected graph 
        for i in range(2, numvert+1):
            x = random.randint(1, i-1)
            S = []
            used_ind = []   # array of used indices when creating set S of randomized indices
            for j in range(x):
                y = random.randint(1, i-1)
                while y in used_ind:
                    y = random.randint(1, i-1)
                used_ind.append(y)
                S.append(y)
            for s in S:
                w = random.randint(10,100)      # Create a random weight for an edge
                self.vertices[i].add_neighbor(self.vertices[s].key, w)      # Create the edge
                self.vertices[self.vertices[s].key].add_neighbor(i, w)
    
    # Adds a vertex to a graph
    def add_vertex(self, vertex):
        self.vertices[vertex.key] = vertex

    # Breadth-First Search implementation 
    def BFS(self):
        Q = []      
        added = []      # Array used to tag vertices as "added_to_queue"
        sum_weight = 0
        vertex = self.vertices[random.randint(1, len(self.vertices)-1)]     # Start BFS at random vertex within the graph
        Q.append(vertex) 
        added.append(vertex.key)

        while len(Q) != 0:
            x = Q[0]
            Q.remove(Q[0])
            for y in x.neighbors:
                if y not in added:      # Loop through all edges except the ones already traversed 
                    Q.append(self.vertices[y])
                    added.append(y)
                    sum_weight += x.neighbors[y]    # Keep track of total weight of selected edges
        return sum_weight
        
    # PRIM algorithm implementation 
    def PRIM(self):
        S = []
        vertex = self.vertices[random.randint(1, len(self.vertices)-1)]     # Start at random vertex within the graph
        T = []
        T.append(vertex)    # add vertex to set of used vertices
        Q = []
        sum_weight = 0

        # Initialize Q set of unused vertices
        for i in self.vertices:
            if self.vertices[i].key != vertex.key:
                Q.append(i)   

        # End the loop when reach n-1 edges as that is the amount spanning tree must have
        while len(S) < len(self.vertices)-1:
            min_weight = 10000      # Pre-determined weight cap to intialize min_weight variable

            # Find the least-weight edge with one end in T and one end in Q
            for x in T:
                for y in x.neighbors:
                    if y in Q:
                        temp = min_weight
                        min_weight = min(min_weight, x.neighbors[y])     
                        if temp != min_weight:      # If the min_weight variable changed, then the current edge is saved
                            e = (x.key,y)
            S.append(e)
            T.append(self.vertices[e[1]])
            Q.remove(e[1])
            sum_weight += self.vertices[e[0]].neighbors[e[1]]       # Record the total weight of all edges traversed 
        return sum_weight

# Comparison of the Breadth-First Search algorithm against the PRIM algorithm
def BFSvPRIM(k):
    n_arr = [20, 40, 60]    # Num of vertices in each test graph
    
    for n in n_arr:
        sum = 0
        for i in range(k):
            g = Graph(n)
            B = g.BFS()
            P = g.PRIM()
            Diff = ((float)(B - P) / P) * 100
            sum += Diff
        average = round(sum / k)
        print('Average for ' + str(n) + ' vertices: ' + str(average) + '%')



# Manually places each vertex and edge to create test graph
def initGraph():
    g = Graph(0)

    for i in range(6):
        v = Vertex(i)
        g.add_vertex(v)

    g.vertices[0].add_neighbor(1, 15)
    g.vertices[0].add_neighbor(3, 7)
    g.vertices[0].add_neighbor(4, 10)
    g.vertices[1].add_neighbor(0, 15)
    g.vertices[1].add_neighbor(2, 9)
    g.vertices[1].add_neighbor(3, 11)
    g.vertices[1].add_neighbor(5, 9)
    g.vertices[2].add_neighbor(1, 9)
    g.vertices[2].add_neighbor(4, 12)
    g.vertices[2].add_neighbor(5, 7)
    g.vertices[3].add_neighbor(0, 7)
    g.vertices[3].add_neighbor(1, 11)
    g.vertices[3].add_neighbor(4, 8)
    g.vertices[3].add_neighbor(5, 14)
    g.vertices[4].add_neighbor(0, 10)
    g.vertices[4].add_neighbor(2, 12)
    g.vertices[4].add_neighbor(3, 8)
    g.vertices[4].add_neighbor(5, 8)
    g.vertices[5].add_neighbor(1, 9)
    g.vertices[5].add_neighbor(2, 7)
    g.vertices[5].add_neighbor(3, 14)
    g.vertices[5].add_neighbor(4, 8)
    return g

def main():
    # Initialize test graph
    g = initGraph()
    
    # Test BFS and PRIM algorithms using test graph
    print('BFS test: ')
    print(g.BFS())
    print('PRIM test: ')
    print(g.PRIM())

    # Compare BFS against the PRIM algorithm with k = 5
    BFSvPRIM(5)
main()