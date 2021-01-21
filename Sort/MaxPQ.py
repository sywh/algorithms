class ArrayMaxPQ:
    def __init__(self, max) -> None:
        self.a = [None]  # init len == 1
        self.N = 0

    def insert(self, v):
        if self.N == len(self.a):
            self.resize(len(self.a) * 2)
        self.a[self.N] = v
        self.N += 1

    def max(self):
        max = self.a[0]
        for i in range(1, self.N):
            if self.a[i] > max:
                max = self.a[i]
        return max

    def delMax(self):
        max = self.N - 1
        for i in range(self.N - 1):
            if self.a[i] > self.a[max]:
                max = i
        self.exch(self.a, max, self.N - 1)

        item = self.a[self.N - 1]
        self.a[self.N - 1] = None
        self.N -= 1

        if self.N > 0 and self.N == len(self.a) // 4:
            self.resize(len(self.a) // 2)
        return item

    def exch(self, a, i, j):
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def resize(self, max: int):
        tmp = [None] * max
        for i in range(self.N):
            tmp[i] = self.a[i]
        self.a = tmp


class MaxPQ:
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

    def delMax(self):
        max = self.pq[1]
        self.exch(1, self.N)
        self.N -= 1
        self.pq[self.N + 1] = None
        self.sink(1)
        return max

    def swim(self, k):
        while k > 1 and self.less(k // 2, k):
            self.exch(k // 2, k)
            k = k // 2

    def sink(self, k):
        while 2 * k <= self.N:
            j = 2 * k
            if j < self.N and self.less(j, j + 1):
                j += 1
            if self.less(k, j):
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
