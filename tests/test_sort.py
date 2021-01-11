import sys

from Fundamentals.Transaction import Transaction
from Sort.Insertion import Insertion
from Sort.MaxPQ import MaxPQ
from Sort.Merge import Merge, MergeBU
from Sort.Quick import Quick
from Sort.Selection import Selection
from Sort.SortCompare import SortCompare
from stdlib.StdIn import InStream


def test_sort(st):
    a = list("QUICKSORTEXAMPLE")
    st.sort(a)
    print(a)


def test_selection():
    st = Selection()
    test_sort(st)


def test_insertion():
    st = Insertion()
    test_sort(st)


def test_quick():
    st = Quick()
    test_sort(st)


def test_merge():
    st = Merge()
    test_sort(st)


def test_mergeBU():
    st = MergeBU()
    test_sort(st)


def test_sortCompare():
    alg1 = sys.argv[1]
    alg2 = sys.argv[2]
    N = int(sys.argv[3])
    T = int(sys.argv[4])

    cmp = SortCompare()

    t1 = cmp.timeRandomInput(alg1, N, T)
    t2 = cmp.timeRandomInput(alg2, N, T)
    print("For {} random doubles".format(N))
    print("{} is {} times faster than {}".format(alg1, t2 / t1, alg2))


def test_maxPQ():
    M = int(sys.argv[1])
    pq = MaxPQ(M + 1)  # M + 1 is absolutely suitable for TopM
    instream = InStream()
    while instream.hasNextLine():
        pq.insert(Transaction(instream.readLine()))
        if pq.size() > M:
            pq.delMax()
    stack = []
    while not pq.isEmpty():
        stack.append(pq.delMax())
    for i in stack:
        print(i)


if __name__ == "__main__":
    # test_selection()
    # test_insertion()
    # test_sortCompare()
    # test_merge()
    # test_mergeBU()
    test_maxPQ()
