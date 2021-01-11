import random

from Fundamentals.Stopwatch import Stopwatch

from Sort.Heap import Heap
from Sort.Insertion import Insertion
from Sort.Merge import Merge
from Sort.Quick import Quick
from Sort.Selection import Selection
from Sort.Shell import Shell


class SortCompare:
    def __init__(self) -> None:
        self.insertion = Insertion()
        self.selection = Selection()
        self.shell = Shell()
        self.merge = Merge()
        self.quick = Quick()
        self.heap = Heap()

    def time(self, alg, a):
        timer = Stopwatch()
        if alg == "Insertion":
            self.insertion.sort(a)
        if alg == "Selection":
            self.selection.sort(a)
        if alg == "Shell":
            self.shell.sort(a)
        if alg == "Merge":
            self.merge.sort(a)
        if alg == "Quick":
            self.quick.sort(a)
        if alg == "Heap":
            self.heap.sort(a)
        return timer.elapsedTime()

    def timeRandomInput(self, alg, N, T):
        total = 0.0
        a = []
        for t in range(T):
            for i in range(N):
                a.append(random.random())
            total += self.time(alg, a)
        return total
