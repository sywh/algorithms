class WeightedQuickUnionUF:
    def __init__(self, N: int):
        self._count = N
        self.id = [i for i in range(N)]
        self.sz = [1 for i in range(N)]

    def find(self, p: int):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p: int, q: int):
        i = self.find(p)
        j = self.find(q)
        if (i == j):
            return 
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        self._count -= 1

    def connected(self, p: int, q: int):
        return self.find(p) == self.find(q)

    def count():
        return self._count