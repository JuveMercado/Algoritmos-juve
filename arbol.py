class Graph(object):

    def __init__(self,*args,**kwargs):
        self.node_neighbors = {}
        self.visited = {}

    def add_nodes(self,nodelist):

        for node in nodelist:
            self.add_node(node)

    def add_node(self,node):
        if not node in self.nodes():
            self.node_neighbors[node] = []

    def add_edge(self,edge):
        u,v = edge
        if(v not in self.node_neighbors[u]) and ( u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)

            if(u!=v):
                self.node_neighbors[v].append(u)

    def nodes(self):
        return self.node_neighbors.keys()

    def depth_first_search(self,root=None):
        order = []
        def dfs(node):
            self.visited[node] = True
            order.append(node)
            self.node_neighbors[node].sort()
            for n in self.node_neighbors[node]:
                if not n in self.visited:
                    dfs(n)


        if root:
            dfs(root)

        for node in self.nodes():
            if not node in self.visited:
                dfs(node)

        #print(order)
        return order

if __name__ == '__main__':
    g = Graph()
    node_num=int(input())#Número de vértices
    #node_c=input().split(',')
    #g.add_nodes(i for i in node_c)
    g.add_nodes([i+1 for i in range(node_num)])
    vec_num=int(input())# Número de lados
    for i in range(vec_num):
        g.add_edge(tuple(int(n) for n in input().split(',')))

    #print("nodes:", g.nodes())

    order = g.depth_first_search(1)
    for i in order:
        print(i,end=' ')
