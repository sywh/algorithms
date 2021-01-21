class BoyerMoore:
    def __init__(self, pat) -> None:
        self.pat = pat
        M = len(pat)
        R = 256
        self.right = [-1 for _ in range(R)]  # char not in pat -> -1
        for j in range(M):
            self.right[pat[j]] = j  # char in pat, rightmost pos of char

    def search(self, txt):
        N = len(txt)
        M = len(self.pat)
        i, skip = 0, 0
        while i <= N - M:
            skip = 0
            for j in reversed(range(0, M)):
                if self.pat[j] != txt[i + j]:
                    skip = j - self.right[txt[i + j]]  # equivalent to pat go back
                    if skip < 1:
                        skip = 1
                    break
            if skip == 0:
                return i
            i += skip  # more efficient than i += 1 every time
        return N
