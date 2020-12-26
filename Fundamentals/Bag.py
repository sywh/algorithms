
from utils.base import Node, ListIterator

class Bag:
    def __init__(self):
        self.first = None
        self.N = 0

    def isEmpty(self):
        return self.N == 0
        # or self.first == None

    def size(self):
        return self.N

    def add(self, item):
        oldfirst = self.first
        self.first = Node(item, oldfirst)

    def __iter__(self):
        return ListIterator(self.first)  # ListIterator should implement next method

    def __str__(self):
        return " ".join(str(i) for i in self)

