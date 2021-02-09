from Graph.Graph import Graph


class Cycle:
    def __init__(self, G: Graph) -> None:
        self._hasCycle = False
        self.marked = [False for _ in range(G.V())]
        for s in range(G.V()):
            if not self.marked[s]:
                self.dfs(G, s, s)

    def dfs(self, G: Graph, v: int, u: int):
        self.marked[v] = True  # remember to mark it!
        for w in G.adj(v):
            if not self.marked[w]:
                self.dfs(G, w, v)
            else:
                if w != u:
                    self._hasCycle = True

    def hasCycle(self):
        return self._hasCycle
