class BinarySearchST:
    def __init__(self, capacity):
        self._keys = [None] * capacity  # avoid compare between None and str
        self._vals = [None] * capacity
        self.N = 0

    def put(self, key, val):
        r = self.rank(key)

        # judge index r before using it in self._keys[r]
        if r < self.N and self._keys[r] == key:
            self._vals[r] = val
        else:
            for i in reversed(range(r + 1, self.N + 1)):
                self._keys[i] = self._keys[i - 1]
                self._vals[i] = self._vals[i - 1]
            self._keys[r] = key
            self._vals[r] = val
            self.N += 1

    def get(self, key):
        r = self.rank(key)
        if r < self.N and self._keys[r] == key:
            return self._vals[r]
        else:
            return None

    def delete(self, key):
        r = self.rank(key)
        if r < self.N and self._keys[r] == key:
            del self._keys[r]
            del self._vals[r]
            self.N -= 1
        else:
            print("key {} is not in ST".format(key))

    def contains(self, key):
        r = self.rank(key)
        if r < self.N and self._keys[r] == key:
            return True
        else:
            return False

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def min(self):
        return self._keys[0]

    def max(self):
        return self._keys[self.size() - 1]

    def floor(self, key):
        r = self.rank(key)
        if 0 < r < self.N:
            if self._keys[r] == key:
                return key
            else:
                return self._keys[r - 1]
        elif r == self.N:
            return self._keys[-1]
        elif r == 0:
            if self._keys[r] == key:
                return key
            else:
                return None

    def ceiling(self, key):
        r = self.rank(key)
        return self._keys[r]

    def select(self, k):
        return self._keys[k]

    def rank(self, key):  # how about duplicate keys?
        lo, hi = 0, self.N - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self._keys[mid] < key:
                lo = mid + 1
            elif self._keys[mid] > key:
                hi = mid - 1
            else:
                return mid
        return lo

    def deleteMin(self):
        del self._keys[0]
        del self._vals[0]

    def deleteMax(self):
        del self._keys[-1]
        del self._vals[-1]

    def _size(self, lo, hi):  # TODO: fix bug
        return self.rank(hi) - self.rank(lo)

    def range_keys(self, lo, hi):
        _keys = []
        for i in range(self.rank(lo), self.rank(hi)):
            _keys.append(self._keys[i])

        if self.contains(hi):
            _keys.append(hi)

        return _keys

    def keys(self):
        return self.range_keys(self.min(), self.max())
