import sys

from Searching.SequentialSearchST import SequentialSearchST
from stdlib import stdio
from stdlib.StdIn import InStream


def test_bahavior():
    st = SequentialSearchST()
    val = 0

    while not stdio.isEmpty():
        k = stdio.readString()
        st.put(k, val)
        val += 1

    # print(st)
    for key in st.keys():
        print(key, st.get(key))


def test_performance():
    minlen = int(sys.argv[1])

    st = SequentialSearchST()
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
    # test_bahavior()
    test_performance()
