from collections import defaultdict


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        new_root.height = 1 + \
            max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        new_root.height = 1 + \
            max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root


def best_fit(items, bin_size):
    bins = defaultdict(list)
    tree = AVLTree()

    for item in items:
        if tree.root and tree.root.key >= item:
            node = tree.root
            while node.left:
                node = node.left
            bin_id = id(node)
            bins[bin_id].append(item)
            node.key -= item
            if node.key == 0:
                tree.root = tree._delete(tree.root, node.key)
            else:
                tree.root = tree._insert(tree.root, node.key)
        else:
            bin_id = len(bins)
            bins[bin_id].append(item)
            tree.insert(bin_size - item)

    return bins.values()
