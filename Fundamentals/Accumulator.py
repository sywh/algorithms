from stdlib import stddraw


class Accumulator:
    def __init__(self):
        self.total = 0
        self.N = 0

    def addDataValue(self, val):
        self.total += val
        self.N += 1

    def mean(self):
        return self.total / self.N

    def __str__(self):
        return "Mean (" + str(self.N) + " values): " + "{}".format(self.mean())


class VisualAccumulator:
    def __init__(self, trials, max):
        self.total = 0
        self.N = 0
        stddraw.setXscale(0, trials)
        stddraw.setYscale(0, max)
        stddraw.setPenRadius(0.005)

    def addDataValue(self, val):
        self.total += val
        self.N += 1
        stddraw.setPenColor(stddraw.DARK_GREEN)
        stddraw.point(self.N, val)
        stddraw.setPenColor(stddraw.DARK_RED)
        stddraw.point(self.N, self.mean())

    def mean(self):
        return self.total / self.N

    def __str__(self):
        return "Mean (" + self.N + " values): " + "{}".format(self.mean())
