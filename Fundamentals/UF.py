class UF:
    def __init__(self, N: int):
        self._count = N
        self.id = [i for i in range(N)]

    def union(self, p: int, q: int):  # add connection between p and q
        pID = self.find(p)
        qID = self.find(q)

        if pID == qID:
            return
        
        for i in range(len(self.id)):
            if self.id[i] = pID:
                self.id[i] = qID
        self._count -= 1

    def find(self, p: int):  # find the identifier of the componet that p belongs to
        return self.id[p]

    def connected(self, p: int, q: int):
        return self.find(p) == self.find(q)

    def count(self):  # num of connected components
        return self._count