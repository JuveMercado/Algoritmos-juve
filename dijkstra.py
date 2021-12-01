import sys
 
from collections import defaultdict

estacionesMetro = [
'El Rosario',
'Instituto del Petroleo',
'Tacuba',
'Hidalgo',
'Tacubaya', 
'Deportivo 18 de Marzo',
'Centro Medico',
'Mixcoac',
'Balderas',
'Bellas Artes',
'Guerrero',
'Martin Carrera',
'Zapata',
'Chabacano',
'Salto del Agua',
'Garibaldi',
'La Raza', 
'Pino Suarez',
'Consulado',
'Candelaria', 
'Ermita',
'Santa Anita',
'Oceania',
'Morelos',
'San Lazaro',
'Jamaica',
'Atlalilco', 
'Pantitlan']

class Graph:
 
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        #agregar un Edge al grafo
        self.graph[u].append(v)
        self.V = v

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = sys.maxsize
 
        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
 
        return min_index
 
    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
 
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                    dist[y] > dist[x] + self.graph[x][y]:
                        dist[y] = dist[x] + self.graph[x][y]
 
        self.printSolution(dist)
 
# Driver program
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 15)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 11)
g.addEdge(3, 12)
g.addEdge(4, 5)
g.addEdge(4, 6)
g.addEdge(4, 9)
g.addEdge(5, 7)
g.addEdge(5, 8)
g.addEdge(5, 9)
g.addEdge(6, 7)
g.addEdge(7, 25)
g.addEdge(8, 21)
g.addEdge(8, 10)
g.addEdge(8, 25)
g.addEdge(8, 26)
g.addEdge(9, 3)
g.addEdge(9, 10)
g.addEdge(11, 10)
g.addEdge(11, 21)
g.addEdge(12, 13)
g.addEdge(13, 11)
g.addEdge(12, 14)
g.addEdge(14, 1)
g.addEdge(14, 15)
g.addEdge(14, 17)
g.addEdge(15, 16)
g.addEdge(17, 16)
g.addEdge(17, 18)
g.addEdge(17, 19)
g.addEdge(18, 23)
g.addEdge(19, 13)
g.addEdge(19, 20)
g.addEdge(20, 18)
g.addEdge(20, 23)
g.addEdge(21, 10)
g.addEdge(21, 22)
g.addEdge(22, 19)
g.addEdge(22, 20)
g.addEdge(23, 24)
g.addEdge(24, 8)
g.addEdge(24, 22)
g.addEdge(25, 27)
g.addEdge(26, 24)
g.addEdge(27, 26)
 
g.dijkstra(28)
 
# This code is contributed by Divyanshu Mehta