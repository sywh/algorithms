import sys

from stdlib.StdIn import InStream
from Strings.Alphabet import Alphabet
from Strings.Brute import search1, search2
from Strings.KMP import KMP


def test_alphabet():
    alpha = Alphabet(sys.argv[1])
    R = alpha.R()
    count = [0 for _ in range(R)]

    instream = InStream()
    s = instream.readAll()
    N = len(s)
    for i in range(N):
        if alpha.contains(s[i]):
            count[alpha.toIndex(s[i])] += 1

    for c in range(R):
        print(alpha.toChar(c), " ", count[c])


def test_match():
    txts = ["ABACADABRAC", "AAAAAAAAAB", "ABAAAABAAAAAAAAA"]
    pats = ["ABRA", "AAAAB", "BAAAAAAAAA"]
    for txt, pat in zip(txts, pats):
        # pos = search1(pat, txt)
        pos = search2(pat, txt)
        print(pos)


def test_kmp():
    txts = ["BCBAABACAABABACAA"]
    pats = ["ABABAC"]
    for txt, pat in zip(txts, pats):
        print("text:   ", txt)
        kmp = KMP(pat)
        offset = kmp.search(txt)
        print(("pattern:" + " " * offset), pat)


if __name__ == "__main__":
    # test_alphabet()
    # test_match()
    test_kmp()
