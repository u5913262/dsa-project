class kruskleMST:

    graph = []
    def __init__(self,vertices):
        self.vertices = vertices

    def find(self, parent, v):
        if parent[v] == v:
            return v
        return self.find(parent, parent[v])

    def union(self, parent, rank, a, b):
        root1 = self.find(parent, a)
        root2 = self.find(parent, b)

        if root1 != root2:
            if rank[root2] < rank[root1]:
                parent[root1] = root2
            else:
                parent[root2] = root1
        if rank[root1] == rank[root2]:
            rank[root2] += 1

    def kruskle(self):
        parent = [] ; rank = []
        self.graph =  sorted(self.graph, key=lambda i: i[2])

        for n in range(self.vertices):
            parent.append(n)
            rank.append(0)

        result =[]
        i = 0
        k = 0
        while k < self.vertices -1 :
            v1,v2,weight =  self.graph[i]
            a = self.find(parent, v1)
            b = self.find(parent ,v2)
            i += 1

            if a != b:
                result.append([v1,v2,weight])
                self.union(parent, rank, a, b)
                k += 1

        for v1,v2,weight in result:
            print ("%d => %d, %d" % (v1,v2,weight))

    def addEdge(self,v1,v2,weight):
        self.graph.append([v1,v2,weight])

graph = kruskleMST(5)

graph.addEdge(0, 1, 10)
graph.addEdge(0, 2, 6)
graph.addEdge(0, 3, 5)
graph.addEdge(1, 3, 15)
graph.addEdge(2, 3, 4)
graph.addEdge(3, 4, 3)
graph.addEdge(3, 1, 5)
graph.addEdge(5, 3, 12)

graph.kruskle()
