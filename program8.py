# program8.py
# B-Tree Implementation (Insert + Display)

class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t                      # Minimum degree
        self.leaf = leaf                # True/False
        self.keys = []                  # Keys stored in node
        self.children = []              # Child pointers

    def insert_non_full(self, key):
        i = len(self.keys) - 1

        # Case 1: If current node is leaf
        if self.leaf:
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key

        # Case 2: Not a leaf
        else:
            while i >= 0 and key < self.keys[i]:
                i -= 1

            i += 1

            # If the child is full, split it
            if len(self.children[i].keys) == (2 * self.t - 1):
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1

            self.children[i].insert_non_full(key)

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BTreeNode(t, y.leaf)

        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys[t - 1])

        z.keys = y.keys[t:(2 * t - 1)]
