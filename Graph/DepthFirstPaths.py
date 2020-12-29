from Graph.Graph import Graph


class DepthFirstPaths:
    def __init__(self, graph, s):
        self._marked = [False] * graph.V()  # marked like chalk
        self.edgeTo = [None] * graph.V()  # act like a tree
        self.dfs(graph, s)

    def dfs(self, graph, v):  # recursive
        self._marked[v] = True
        for w in graph.adj(v):
            if not self._marked[w]:
                self.edgeTo[w] = v
                self.dfs(graph, w)

    def hasPathTo(self, v):
        return self._marked[v]

    def pathTo(self, v):
        path = []
        while v != None:
            path.append(v)
            v = self.edgeTo[v]
        return path[::-1]


class DepthFirstPathsIterative:
    def __init__(self, graph, s):
        self._marked = [False] * graph.V()
        self.edgeTo = [None] * graph.V()
        self.dfs(graph, s)

    def dfs(self, graph, v):  # iterative
        stack = []
        stack.append(v)

        while len(stack):
            v = stack[-1]
            stack.pop()
            self._marked[v] = True

            for w in graph.adj(v):
                if not self._marked[w]:
                    stack.append(w)

    def hasPathTo(self, v):
        return self._marked[v]

    def pathTo(self, v):
        path = []
        while v != None:
            path.append(v)
            v = self.edgeTo[v]
        return path



