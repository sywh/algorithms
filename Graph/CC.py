
from Graph.Graph import Graph

class CC:
    def __init__(self, graph):
        self._marked = [False] * graph.V()
        self._id = [None] * graph.V()
        self._count = 0

        for v in range(graph.V()):
            if not self._marked[v]:
                self.dfs(graph, v)
                self._count += 1

    def dfs(self, graph, v):
        self._marked[v] = True
        self._id[v] = self._count

        for w in graph.adj(v):
            if not self._marked[w]:
                self.dfs(graph, w)

    def connected(self, v, w):
        return self._id[v] == self._id[w]

    def count(self):
        return self._count

    def id(self, v):
        return self._id[v]
    
