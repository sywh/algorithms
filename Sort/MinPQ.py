class MinPQ:
    def __init__(self, max):  # how about resize?
        self.pq = [None] * (max + 1)  # pq[0] is not used
        self.N = 0

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def insert(self, v):
        self.N += 1
        self.pq[self.N] = v
        self.swim(self.N)

    def delMin(self):
        min = self.pq[1]
        self.exch(1, self.N)
        self.N -= 1
        self.pq[self.N + 1] = None
        self.sink(1)
        return min

    def swim(self, k):
        while k > 1 and self.less(k, k // 2):
            self.exch(k // 2, k)
            k = k // 2

    def sink(self, k):
        while 2 * k <= self.N:
            j = 2 * k
            if j < self.N and self.less(j + 1, j):
                j += 1
            if self.less(j, k):
                self.exch(k, j)
            else:
                break
            k = j

    def exch(self, i, j):
        tmp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = tmp

    def less(self, i, j):
        return self.pq[i] < self.pq[j]
