
from Graph.Graph import Graph


class DepthFirstSearch:
    def __init__(self, graph, s):
        self._marked = [False] * graph.V()  # marked like chalk
        self._count = 0
        self.dfs(graph, s)

    def dfs(self, graph, v):  # recursive 
        self._marked[v] = True
        self._count += 1
        for w in graph.adj(v):
            if not self._marked[w]:
                self.dfs(graph, w)

    def marked(self, w):
        return self._marked[w]

    def count(self):
        return self._count

        
