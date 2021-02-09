from typing import List


class SparseVector:
    def __init__(self) -> None:
        self.st = {}

    def size(self):
        return self.st.size()

    def put(self, i: int, x: float):
        self.st[i] = x

    def get(self, i: int):
        if i not in self.st:
            return 0.0
        else:
            return self.st[i]

    def dot(self, that: List[float]):
        sum = 0.0
        for i in self.st:
            sum += that[i] * self.get(i)
        return sum
