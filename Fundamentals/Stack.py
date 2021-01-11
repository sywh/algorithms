
class ResizingArrayStack:
    def __init__(self):
        self.a = [None]  # stack elements
        self.N = 0  # number of elements

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def resize(self, max: int):  # move stack to a new array size of max
        tmp = [None] * max
        for i in range(self.N):
            tmp[i] = self.a[i]
        self.a = tmp

    def push(self, item):
        if (self.N == len(self.a)):
            self.resize(2* len(self.a))
        self.a[self.N] = item
        self.N += 1

    def pop(self):
        self.N -= 1
        item = self.a[self.N]
        self.a[self.N] = None
        if (self.N > 0 and self.N == len(self.a) // 4):
            self.resize(len(self.a) // 2)
        return item

    def __iter__(self):
        cur = self.N - 1
        while cur >= 0:
            yield self.a[cur]  # yield grammer is always used in iterator
            cur -= 1


