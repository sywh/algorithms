from Graph.EdgeWeightedGraph import EdgeWeightedGraph
from Sort.IndexMinPQ import IndexMinPQ


class PrimMST:
    def __init__(self, G: EdgeWeightedGraph) -> None:
        self.edgeTo = [None for _ in range(G.V())]  # edge
        self.distTo = [float('inf') for _ in range(G.V())]  # weight
        self.marked = [False for _ in range(G.V())]  # boolean
        self.pq = IndexMinPQ(G.V())
        self.mst = []

        self.distTo[0] = 0.0
        self.pq.insert(0, 0.0)
        while not self.pq.isEmpty():
            self.visit(G, self.pq.delMin())

    def visit(self, G: EdgeWeightedGraph, v: int):
        self.marked[v] = True
        self.mst.append(self.edgeTo[v])
        for e in G.adj(v):
            w = e.other(v)
            if self.marked[w]:  # invalid edge
                continue
            if e.weight() < self.distTo[w]:
                self.edgeTo[w] = e
                self.distTo[w] = e.weight()
                if self.pq.contains(w):
                    self.pq.change(w, self.distTo[w])  # just contain the min edge
                else:
                    self.pq.insert(w, self.distTo[w])
    
    def edges(self):
        return self.mst[1:]

    def weight(self):
        return sum([e.weight() for e in self.edges()])
            


