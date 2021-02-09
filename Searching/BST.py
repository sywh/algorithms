class Node:
    def __init__(self, key, val, N) -> None:
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.N = N


class BST:
    def __init__(self) -> None:
        self.root = None

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, node, key, val) -> Node:
        if node == None:
            return Node(key, val, 1)
        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.N = self._size(node.left) + self._size(node.right) + 1
        return node

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, node, key):
        if node == None:
            return None
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    def size(self):
        return self._size(self.root)

    def _size(self, x):
        if x == None:
            return 0
        else:
            return x.N

    def min(self):
        return self._min(self.root).key

    def _min(self, node) -> Node:
        if node.left == None:
            return node
        return self._min(node.left)

    def max(self):
        return self._max(self.root).key

    def _max(self, node) -> Node:
        if node.right == None:
            return node
        return self._max(node.right)

    def floor(self, key):
        node_x = self._floor(self, self.root, key)
        if node_x == None:
            return None
        return node_x.key

    def _floor(self, node, key) -> Node:  # if all of tree node.key > key, return None
        if node == None:
            return None
        if key < node.key:
            return self._floor(node.left, key)
        elif key > node.key:
            node_t = self._floor(node.right, key)
            if node_t != None:
                return node_t
            else:
                return node
        else:
            return node

    def ceiling(self, key):
        node_x = self._ceiling(self.root, key)
        if node_x == None:
            return None
        return node_x.key

    def _ceiling(self, node, key) -> Node:
        if node == None:
            return None
        if key < node.key:
            node_t = self._ceiling(node.left, key)
            if node_t != None:
                return node_t
            else:
                return node
        elif key > node.key:
            return self._ceiling(node.right, key)
        else:
            return node

    def select(self, k):
        return self._select(self.root, k).key

    def _select(self, node, k):
        if node == None:
            return None
        t = self._size(node.left)
        if t > k:  # good realization
            return self._select(node.left, k)
        elif t < k:
            return self._select(node.right, k - t - 1)
        else:
            return node

    def rank(self, key):
        return self._rank(self.root, key)

    def _rank(self, node, key):
        if node == None:
            return 0

        if key < node.key:
            return self._rank(node.left, key)
        elif key > node.key:
            return self._size(node.left) + 1 + self._rank(node.right, key)
        else:
            return self._size(node.left)

    def contains(self, key):
        r = self.rank(key)
        if r < self.size() and self.select(r) == key:
            return True
        else:
            return False

    def deleteMin(self):
        self.root = self._deleteMin(self.root)

    def _deleteMin(self, node) -> Node:  # NOTE: return a tree that have deleted mininum
        if node.left == None:
            return node.right
        node.left = self._deleteMin(node.left)
        node.N = self._size(node.left) + self._size(node.right) + 1
        return node

    def deleteMax(self):
        self.root = self._deleteMax(self.root)

    def _deleteMax(self, node):
        if node.right == None:
            return node.left
        node.right = self._deleteMax(node.right)
        node.N = self._size(node.left) + self._size(node.right) + 1

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):  # quite difficult
        if node == None:
            return None

        if key > node.key:
            node.right = self._delete(node.right, key)
        elif key < node.key:
            node.left = self._delete(node.left, key)
        else:
            # TODO: figure out python copy and reference of object
            # and garbage collection mechanism
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            t = node
            node = self._min(node.right)
            node.left = t.left
            node.right = self._deleteMin(t.right)

        node.N = self._size(node.left) + self._size(node.right) + 1
        return node

    def keys(self):
        return self._keys(self.min(), self.max())

    def _keys(self, lo, hi):
        queue = []
        self.node_keys(self.root, queue, lo, hi)
        return queue

    def node_keys(self, node, queue, lo, hi):
        if node == None:
            return

        # quite interesting! it is exactly inorder traversal
        if node.key > lo:
            self.node_keys(node.left, queue, lo, hi)
        if node.key >= lo and node.key <= hi:
            queue.append(node.key)
        if node.key < hi:
            self.node_keys(node.right, queue, lo, hi)
