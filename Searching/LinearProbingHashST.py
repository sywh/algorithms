class LinearProbingHashST:
    def __init__(self, M=16):
        self.M = M
        self.N = 0
        self.keys = [None for _ in range(self.M)]
        self.vals = [None for _ in range(self.M)]

    def hash(self, key):
        return (hash(key) & 0x7FFFFFFF) % self.M

    def resize(self, cap: int):
        t = LinearProbingHashST(cap)
        for i in range(self.M):
            if self.keys[i] != None:
                t.put(self.keys[i], self.vals[i])
        self.keys = t.keys
        self.vals = t.vals
        self.M = t.M

    def put(self, key, val):
        if self.N >= self.M // 2:  # utilization < 1/2
            self.resize(2 * self.M)

        i = self.hash(key)
        while self.keys[i] != None:
            if self.keys[i] == key:
                self.vals[i] = val
                return
            i = (i + 1) % self.M
        self.keys[i] = key
        self.vals[i] = val
        self.N += 1

    def get(self, key):
        i = self.hash(key)
        while self.keys[i] != None:
            if self.keys[i] == key:
                return self.vals[i]
            i = (i + 1) % self.M
        return None

    def contains(self, key):
        if self.get(key) != None:
            return True
        return False

    def keys(self):
        for key in self.keys:
            if key != None:
                yield key

    def delete(self, key):
        if not self.contains(key):
            return

        i = self.hash(key)
        while (
            self.keys[i] != key
        ):  # self.keys[i] != None? self.contains have done this!
            i = (i + 1) % self.M

        self.keys[i] = None
        self.vals[i] = None

        i = (i + 1) % self.M
        while self.keys[i] != None:  # why not judge hash same or not first?
            keyToRedo = self.keys[i]
            valToRedo = self.vals[i]
            self.N -= 1
            self.put(keyToRedo, valToRedo)
            i = (i + 1) % self.M
        self.N -= 1
        if self.N > 0 and self.N == self.M // 8:  # utilization > 1/8
            self.resize(self.M // 2)
