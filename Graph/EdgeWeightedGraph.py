from Fundamentals.Bag import Bag

from Graph.Edge import Edge


class EdgeWeightedGraph:
    def __init__(self, V=0) -> None:
        self._V = V
        self._E = 0
        self._adj = [Bag() for _ in range(self._V)]

    def from_stream(self, instream):
        self._V = instream.readInt()
        E = instream.readInt()

        self._adj = [Bag() for _ in range(self._V)]

        for i in range(E):  # TODO: adaptive
            v = instream.readInt()
            w = instream.readInt()
            weight = instream.readFloat()
            self.addEdge(Edge(v, w, weight))

    def V(self):
        return self._V

    def E(self):
        return self._E

    def addEdge(self, e: Edge):
        v = e.either()
        w = e.other(v)  # nice implementation !
        self._adj[v].add(e)
        self._adj[w].add(e)
        self._E += 1

    def adj(self, v):
        return self._adj[v]

    def edges(self):
        b = Bag()
        for v in range(self.V()):
            for e in self.adj(v):
                if e.other(v) > v:
                    b.add(e)
        return b

    def __str__(self) -> str:
        s = ""
        for e in self.edges():
            s += str(e) + "\n"
        return s
