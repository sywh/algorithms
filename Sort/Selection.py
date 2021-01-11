from Sort.Example import Example


class Selection(Example):
    def __init__(self):
        super().__init__()

    # select the minimum and swap with front element
    def sort(self, a):
        N = len(a)
        for i in range(N):
            min = i
            for j in range(i + 1, N):
                if self.less(a[j], a[min]):
                    min = j
            self.exch(a, i, min)
