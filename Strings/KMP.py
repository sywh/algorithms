class KMP:
    def __init__(self, pat: str) -> None:
        # calculate DFA with pat
        self.pat = pat
        M = len(pat)
        R = 256

        self.dfa = [[0 for _ in range(M)] for _ in range(R)]
        self.dfa[ord(pat[0])][0] = 1

        X, j = 0, 1
        while j < M:
            # calculate dfa[][j]
            for c in range(R):
                self.dfa[c][j] = self.dfa[c][X]  # don't match
            self.dfa[ord(pat[j])][j] = j + 1  # match
            X = self.dfa[ord(pat[j])][X]
            j += 1

    def search(self, txt: str):
        N = len(txt)
        M = len(self.pat)
        i, j = 0, 0
        while i < N and j < M:
            j = self.dfa[ord(txt[i])][j]
            i += 1
        if j == M:
            return i - M
        else:
            return N
