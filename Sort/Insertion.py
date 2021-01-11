from Sort.Example import Example


class Insertion(Example):
    def __init__(self):
        super().__init__()

    def sort(self, a):
        N = len(a)
        for i in range(1, N):
            for j in reversed(range(1, i + 1)):  # be careful: i + 1
                if self.less(a[j], a[j - 1]):
                    self.exch(a, j, j - 1)
                else:
                    break
