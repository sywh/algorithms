import sys

from Fundamentals.Accumulator import Accumulator, VisualAccumulator
from Fundamentals.Bag import Bag
from Fundamentals.UF import UF
from stdlib import stdrandom
from stdlib.StdIn import InStream


def test_bag():
    for line in sys.stdin:
        bag = Bag()
        for item in line.split():
            bag.add(item)  # add
        print("size of bag: {}".format(bag.size()))  # size
        print("items:")
        for item in bag:  # iterator
            print(item)
            import ipdb

            ipdb.set_trace()
        print("bag:", bag)  # str


def test_accumulator():
    n = int(sys.argv[1])
    accumulator = Accumulator()
    for i in range(n):
        num = stdrandom.uniformFloat(0, 1)
        accumulator.addDataValue(num)
    print(accumulator)


def test_visual_accumulator():
    n = int(sys.argv[1])
    accumulator = VisualAccumulator(n, 1.0)
    for i in range(n):
        num = stdrandom.uniformFloat(0, 1)
        accumulator.addDataValue(num)
    print(accumulator)


def test_uf():
    instream = InStream()
    N = instream.readInt()
    uf = UF(N)
    while not instream.isEmpty():
        p = instream.readInt()
        q = instream.readInt()
        if uf.connected(p, q):
            continue
        uf.union(p, q)
        print(p, " ", q)
    print(uf.count(), "components")


if __name__ == "__main__":
    # test_bag()
    # test_accumulator()
    # test_visual_accumulator()
    test_uf()
