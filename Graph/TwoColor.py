from Graph.Graph import Graph


class TwoColor:
    def __init__(self, G: Graph) -> None:
        self.isTwoColorable = True
        self.marked = [False for _ in range(G.V())]
        self.color = [False for _ in range(G.V())]
        for s in range(G.V()):
            if not self.marked[s]:
                self.dfs(G, s)

    def dfs(self, G: Graph, v: int):
        self.marked[v] = True
        for w in G.adj(v):
            if not self.marked[w]:
                self.color[w] = not self.color[v]
                self.dfs(G, w)
            else:
                if self.color[w] == self.color[v]:
                    self.isTwoColorable = False

    def isBipartite(self):
        return self.isTwoColorable
