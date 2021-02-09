from Sort.Example import Example


class Merge(Example):
    def __init__(self) -> None:
        super().__init__()

    def sort(self, a):
        # create aux just once
        self.aux = [None for i in range(len(a))]
        self._sort(a, 0, len(a) - 1)

    def _sort(self, a, lo, hi):
        if lo >= hi:
            return

        mid = lo + (hi - lo) // 2
        self._sort(a, lo, mid)
        self._sort(a, mid + 1, hi)
        self.merge(a, lo, mid, hi)

    def merge(self, a, lo, mid, hi):
        for i in range(lo, hi + 1):
            self.aux[i] = a[i]

        i, j = lo, mid + 1
        for k in range(lo, hi + 1):
            if i > mid:  # if, elif, elif, else(right), not if, if, if, if(wrong)
                a[k] = self.aux[j]
                j += 1
            elif j > hi:
                a[k] = self.aux[i]
                i += 1
            elif self.less(self.aux[i], self.aux[j]):
                a[k] = self.aux[i]
                i += 1
            else:
                a[k] = self.aux[j]
                j += 1


class MergeBU(Merge):
    def __init__(self) -> None:
        super().__init__()

    def sort(self, a):  # Great implementation !
        self.aux = [None for i in range(len(a))]
        N = len(a)
        sz = 1

        while sz < N:
            lo = 0
            while lo < N - sz:  # must ensure lo, lo+sz-1, lo+2*sz-1 <= N-1
                self.merge(a, lo, lo + sz - 1, min(lo + 2 * sz - 1, N - 1))
                lo += 2 * sz
            sz += sz
