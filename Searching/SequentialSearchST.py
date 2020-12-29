class Node:
    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next


class NodeIterator:
    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration()
        else:
            key = self.current.key
            self.current = self.current.next
            return key


class SequentialSearchST:
    def __init__(self):
        self.first = None
        self._size = 0

    def get(self, key):
        node = self.first
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return None

    def put(self, key, val):
        node = self.first
        while node:
            if node.key == key:
                node.val = val
                return
            node = node.next
        self.first = Node(key, val, self.first)  # insert as head node
        self._size += 1

    def delete(self, key):
        node = self.first
        next = node.next

        if node.key == key:
            self.first = next
            return

        while next:
            if next.key == key:
                node.next = next.next
                return
            node = next
            next = next.next

    def contains(self, key):
        for k in self.keys():
            if k == key:
                return True
        return False

        """
        node = self.first
        while node:
            if node.key == key:
                return True
        return False
        """

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self._size

    def keys(self):
        return NodeIterator(self.first)

    def __str__(self):
        s = ""
        for key in self.keys():
            s += key + ": " + str(self.get(key)) + "\n"
        return s
