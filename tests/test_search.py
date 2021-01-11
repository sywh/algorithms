import sys

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


if __name__ == "__main__":
    # st = SequentialSearchST()
    # st = BinarySearchST(60)
    # st = BST()
    st = SeparateChainingHashST(97)
    test_bahavior(st)
    # test_performance(st)
