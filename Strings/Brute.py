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
    i, j = 0, 0
    while i < N and j < M:
        if txt[i] == pat[j]:
            j += 1
        else:
            i -= j
            j = 0
        i += 1
    if j == M:
        return i - M
    return N
