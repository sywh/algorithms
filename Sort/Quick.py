import random


class Quick:
    def __init__(self):
        pass

    def sort(self, a):
        random.shuffle(a)
        self._sort(a, 0, len(a) - 1)

    def _sort(self, a, lo, hi):
        if lo >= hi:
            return

        j = self.partition(a, lo, hi)
        self._sort(a, lo, j - 1)
        self._sort(a, j + 1, hi)

    def exch(self, a, lo, hi):
        tmp = a[lo]
        a[lo] = a[hi]
        a[hi] = tmp

    def partition(self, a, lo, hi):
        i, j = lo, hi + 1
        v = a[lo]
        while True:
            while a[i + 1] < v:  # how about duplicated element?
                i += 1
                if i == hi:
                    break
            i += 1  # important
            while a[j - 1] > v:
                j -= 1
                if j == lo:
                    break
            j -= 1
            if i >= j:
                break
            self.exch(a, i, j)
        self.exch(a, lo, j)
        return j
