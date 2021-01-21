class IndexMinPQ:  # refer to https://www.cnblogs.com/nullzx/p/6624731.html
    def __init__(self, max):  # how about resize?
        self.pq = [None] * (max + 1)
        self.qp = [None] * (max + 1)  # inverse of pq: qp[pq[i]] = pq[qp[i]] = i
        self.keys = [None] * (max + 1)  # keys[i] = priority of i
        self.N = 0
        self.max = max

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def contains(self, k):
        assert k >= 0 and k <= self.max
        return self.qp[k] != None

    def insert(self, k: int, item):
        self.N += 1
        self.pq[self.N] = k
        self.qp[k] = self.N
        self.keys[k] = item
        self.swim(self.N)

    def change(self, k: int, item):
        idx = self.qp[k]
        self.keys[k] = item
        self.swim(idx)

    def min(self):
        min = self.pq[1]
        return self.keys[min]

    def delMin(self):
        min = self.pq[1]
        self.exch(1, self.N)
        self.N -= 1
        self.sink(1)
        self.pq[self.N + 1] = None
        self.qp[min] = None
        self.keys[min] = None
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
        # update pq
        tmp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = tmp
        # update qp
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    def less(self, i, j):
        return self.keys[self.pq[i]] < self.keys[self.pq[j]]
