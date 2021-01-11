from Searching.SequentialSearchST import SequentialSearchST


class SeparateChainingHashST:
    def __init__(self, M):
        self.M = M
        self.st = [SequentialSearchST() for _ in range(M)]  # be careful! DO NOT use * M

    def get(self, key):
        m = (hash(key) & 0x7FFFFFFF) % self.M
        return self.st[m].get(key)

    def put(self, key, val):
        m = (hash(key) & 0x7FFFFFFF) % self.M
        self.st[m].put(key, val)

    def delete(self, key):
        m = (hash(key) & 0x7FFFFFFF) % self.M
        self.st[m].delete(key)

    def contains(self, key):
        m = (hash(key) & 0x7FFFFFFF) % self.M
        return self.st[m].contains(key)

    def isEmpty(self):
        for i in range(self.M):
            if not self.st[i].isEmpty():
                return False
        return True

    def size(self):
        s = 0
        for i in range(self.M):
            s += self.st[i].size()
        return s

    def keys(self):
        for i in range(self.M):
            for key in self.st[i].keys():
                yield key

    def resize(self, cap):  # great implementation!
        st = SeparateChainingHashST(cap)
        for key in self.keys():
            val = self.get(key)
            st.put(key, val)

        self.M = cap
        self.st = st
