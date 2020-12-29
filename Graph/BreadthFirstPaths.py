
from Graph.Graph import Graph


class BreadthFirstPaths:
    def __init__(self, graph, s):
        self._marked = [False] * graph.V()
        self.edgeTo = [None] * graph.V()
        self.bfs(graph, s)

    def bfs(self, graph, v):
        queue = []
        queue.append(v)
        self._marked[v] = True

        while len(queue):
            v = queue[0]
            del queue[0]
            for w in graph.adj(v):
                if not self._marked[w]:
                    queue.append(w)
                    self._marked[w] = True
                    self.edgeTo[w] = v

    def hasPathTo(self, v):
        return self._marked[v]

    def pathTo(self, v):
        path = []
        while v != None:
            path.append(v)
            v = self.edgeTo[v]
        return path[::-1]


            
