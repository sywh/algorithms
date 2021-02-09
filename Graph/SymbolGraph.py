from stdlib.StdIn import InStream

from Graph.Graph import Graph


class SymbolGraph:  # nice implementation!
    def __init__(self, stream: str, sp: str) -> None:
        self.st = {}  # name -> index
        instream = InStream(stream)
        while instream.hasNextLine():
            a = instream.readLine().split(sp)
            for i in range(len(a)):
                if a[i] not in self.st:
                    self.st[a[i]] = len(self.st)

        self.keys = [None for _ in range(len(self.st))]  # index -> name
        for name in self.st:
            self.keys[self.st[name]] = name

        self._G = Graph(len(self.st))  # need num of vertex, so read stream twice
        instream = InStream(stream)
        while instream.hasNextLine():
            a = instream.readLine().split(sp)
            v = self.st[a[0]]
            for i in range(1, len(a)):
                self._G.addEdge(v, self.st[a[i]])

    def contains(self, s: str) -> bool:
        return s in self.st

    def index(self, s: str) -> int:
        return self.st[s]

    def name(self, v: int) -> str:
        return self.keys[v]

    def G(self) -> Graph:
        return self._G
