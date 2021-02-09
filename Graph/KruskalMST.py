from Fundamentals.WeightedQuickUnionUF import WeightedQuickUnionUF as UF
from Sort.MinPQ import MinPQ

from Graph.EdgeWeightedGraph import EdgeWeightedGraph


class KruskalMST:
    def __init__(self, G: EdgeWeightedGraph):
        self.mst = []
        self.pq = MinPQ(G.E())
        for e in G.edges():
            self.pq.insert(e)
        self.uf = UF(G.V())

        while not self.pq.isEmpty() and len(self.mst) < G.V() - 1:
            e = self.pq.delMin()
            v = e.either()
            w = e.other(v)
            if self.uf.connected(v, w):  # ignore invalid edge
                continue
            self.uf.union(v, w)
            self.mst.append(e)

    def edges(self):
        return self.mst

    def weight(self):
        return sum([e.weight() for e in self.edges()])
