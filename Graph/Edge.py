class Edge:
    def __init__(self, v: int, w: int, weight: float) -> None:
        self.v = v
        self.w = w
        self._weight = weight

    def weight(self):
        return self._weight

    def either(self):
        return self.v

    def other(self, vertex):
        if vertex == self.v:
            return self.w
        elif vertex == self.w:
            return self.v
        else:
            raise Exception("Inconsistent edge")

    """
    def compareTo(self, that):
        if self.weight < that.weight:
            return -1
        elif self.weight > that.weight:
            return 1
        else:
            return 0
    """

    def __lt__(self, that):
        return self.weight < that.weight

    def __gt__(self, that):
        return self.weight > that.weight

    def __eq__(self, that):
        return self.weight == that.weight

    def __str__(self):
        return "{}-{} {}".format(self.v, self.w, self.weight())
