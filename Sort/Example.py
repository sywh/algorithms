class Example:
    """
    Realize sort algorithms by function may be better than class, but here we select class
    """

    def __init__(self):
        pass

    def sort(self, a):
        pass

    def less(self, v, w):
        return v < w

    def exch(self, a, i, j):
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp

    def show(self, a):
        print(a)

    def isSorted(self, a):
        for i in range(1, len(a)):
            if self.less(a[i], a[i - 1]):
                return False
        return True
