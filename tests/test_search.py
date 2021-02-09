import sys
from typing import List

from Searching.BinarySearchST import BinarySearchST
from Searching.BST import BST
from Searching.SeparateChainingHashST import SeparateChainingHashST
from Searching.SequentialSearchST import SequentialSearchST
from stdlib import stdio
from stdlib.StdIn import InStream


def test_bahavior(st):
    val = 0

    while not stdio.isEmpty():
        k = stdio.readString()
        st.put(k, val)
        val += 1

    for key in st.keys():
        print(key, st.get(key))


def test_performance(st):
    minlen = int(sys.argv[1])

    while not stdio.isEmpty():
        word = stdio.readString()
        if len(word) < minlen:
            continue
        if not st.contains(word):
            st.put(word, 1)
        else:
            st.put(word, st.get(word) + 1)

    max = " "
    st.put(max, 0)
    for key in st.keys():
        if st.get(key) > st.get(max):
            max = key

    print(max, st.get(max))


# application below
def dedup():  # deduplication
    s = set()  # standard python set
    while not stdio.isEmpty():
        key = stdio.readString()
        if key not in s:
            s.add(key)
            print(key)


def whiteFilter(args: List[str]):
    s = set()
    instream = InStream(args[0])
    while not instream.isEmpty():
        s.add(instream.readString())
    while not stdio.isEmpty():
        word = stdio.readString()
        if word in s:
            print(word)


def lookupCSV(args: List[str]):
    st = dict()
    instream = InStream(args[0])
    keyField = int(args[1])
    valField = int(args[2])

    while instream.hasNextLine():
        line = instream.readLine()
        tokens = line.split(",")
        key = tokens[keyField]
        val = tokens[valField]
        st[key] = val

    while not stdio.isEmpty():
        query = stdio.readString()
        if query in st:
            print(st[query])


def lookupIndex(args: List[str]):
    instream = InStream(args[0])
    sp = args[1]
    st, ts = {}, {}
    while instream.hasNextLine():
        a = instream.readLine().split(sp)
        key = a[0]
        for i in range(len(a)):
            val = a[i]
            if key not in st:
                st[key] = []
            if val not in ts:
                ts[val] = []
            st[key].append(val)
            ts[val].append(key)

    while not stdio.isEmpty():
        query = stdio.readLine()
        if query in st:
            for s in st[query]:
                print(s)
        if query in ts:
            for s in ts[query]:
                print(s)


def fileIndex(args: List[str]):
    st = {}
    for filename in args:
        instream = InStream(filename)
        while not instream.isEmpty():
            word = instream.readString()
            if word not in st:
                st[word] = set()
            s = st[word]
            s.add(filename)

    while not stdio.isEmpty():
        query = stdio.readString()
        if query in st:
            for filename in st[query]:
                print(filename)


if __name__ == "__main__":
    # st = SequentialSearchST()
    # st = BinarySearchST(60)
    # st = BST()
    # st = SeparateChainingHashST(97)
    # test_bahavior(st)
    # test_performance(st)
    # dedup()
    # whiteFilter(sys.argv[1:])
    # lookupCSV(sys.argv[1:])
    # lookupIndex(sys.argv[1:])
    fileIndex(sys.argv[1:])
