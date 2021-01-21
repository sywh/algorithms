import math


class Alphabet:
    def __init__(self, s: str) -> None:
        self.s = s

    def toChar(self, index: int):
        return self.s[index]

    def toIndex(self, c: str):  # TODO: str.index(c) implementation in python
        return self.s.index(c)

    def contains(self, c: str):
        if c in self.s:
            return True
        else:
            return False

    def R(self):
        return len(self.s)

    def lgR(self):  # is it useful ? or I misunderstand it ?
        return math.ceil(math.log(self.R(), 2))

    def toIndices(self, s: str) -> list:
        lst = []
        for c in s:
            lst.append(self.toIndex(c))
        return lst

    def toChars(self, indices: list) -> str:
        s = ""
        for index in indices:
            s += self.toChar(index)
        return s
