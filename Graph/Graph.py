
from Fundamentals.Bag import Bag
from stdlib.StdIn import InStream

class Graph:
    def __init__(self, V=0):
        self._V = V  # variable and method name should not be the same
        self._E = 0
        self._adj = []

        for v in range(V):
            self._adj.append(Bag())

    """
    @classmethod
    def Graph(instream, cls):
        cls(instream.readInt())
    """

    def from_stream(self, instream):
        self._V = instream.readInt()
        E = instream.readInt()

        for v in range(self._V):
            self._adj.append(Bag())

        for i in range(E):
            v = instream.readInt()
            w = instream.readInt()
            self.addEdge(v, w)

    def V(self):
        return self._V

    def E(self):
        return self._E

    def addEdge(self, v, w):
        self._adj[v].add(w)
        self._adj[w].add(v)
        self._E += 1

    def adj(self, v):
        return self._adj[v]

    def __str__(self):
        s = ""
        for v in range(self._V):
            s += "V={}:  E=".format(v)
            s += str(self.adj(v))
            s += "\n"
        return s

        


