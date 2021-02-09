from Sort.MinPQ import MinPQ

from Graph.EdgeWeightedGraph import EdgeWeightedGraph


class LazyPrimMST:
    def __init__(self, G: EdgeWeightedGraph) -> None:
        self.pq = MinPQ(G.E())
        self.marked = [False for _ in range(G.V())]
        self.mst = []

        self.visit(G, 0)
        while not self.pq.isEmpty():
            e = self.pq.delMin()  # get edge with min weight
            v = e.either()
            w = e.other(v)
            if self.marked[v] and self.marked[w]:  # skip(delete) invalide edge
                continue
            self.mst.append(e)

            if not self.marked[v]:
                self.visit(G, v)
            if not self.marked[w]:
                self.visit(G, w)

    def visit(self, G: EdgeWeightedGraph, v: int):
        self.marked[v] = True
        for e in G.adj(v):
            if not self.marked[e.other(v)]:
                self.pq.insert(e)

    def edges(self):
        return self.mst

    def weight(self):
        weight = 0
        for e in self.edges():
            weight += e.weight
        return weight
