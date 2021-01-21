def search1(pat: str, txt: str):
    M = len(pat)
    N = len(txt)
    for i in range(N - M + 1):
        j = 0
        while j < M:
            if txt[i + j] == pat[j]:  # index should be i + j for txt
                j += 1
            else:
                break
        if j == M:
            return i
    return N


def search2(pat: str, txt: str):
    M = len(pat)
    N = len(txt)
    i = 0
    while i < N:
        j = 0
        while j < M:
            if txt[i] == pat[j]:
                i += 1
                j += 1
            else:
                i -= j
                break
        if j == M:
            return i - M
        i += 1
    return N
