# program9.py
# Fibonacci Heap Implementation

class Node:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.child = None
        self.left = self
        self.right = self
        self.parent = None
        self.mark = False


class FibonacciHeap:
    def __init__(self):
        self.min = None
        self.total_nodes = 0

    def insert(self, key):
        node = Node(key)

        if self.min is None:
            self.min = node
        else:
            # insert to root list
            node.right = self.min.right
            self.min.right.left = node
            self.min.right = node
            node.left = self.min

            if key < self.min.key:
                self.min = node

        self.total_nodes += 1

    def get_min(self):
        if self.min:
            return self.min.key
        return None

    def extract_min(self):
        z = self.min

        if z:
            if z.child:
                child = z.child
                while True:
                    next_child = child.right
                    child.parent = None

                    # add to root list
                    child.left = self.min
                    child.right = self.min.right
                    self.min.right.left = child
                    self.min.right = child

                    if next_child == z.child:
                        break
                    child = next_child

            z.left.right = z.right
            z.right.left = z.left

            if z == z.right:
                self.min = None
            else:
                self.min = z.right
                self._consolidate()

            self.total_nodes -= 1
            return z.key

        return None

    def decrease_key(self, node, new_key):
        if new_key > node.key:
            print("New key is greater than current key!")
            return

        node.key = new_key
        parent = node.parent

        if parent and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)

        if node.key < self.min.key:
            self.min = node

    def _cut(self, n, parent):
        if parent.child == n:
            if n.right != n:
                parent.child = n.right
            else:
                parent.child = None

        n.left.right = n.right
        n.right.left = n.left
        parent.degree -= 1

        n.right = self.min.right
        self.min.right.left = n
        self.min.right = n
        n.left = self.min
        n.parent = None
        n.mark = False

    def _cascading_cut(self, node):
        p = node.parent
        if p:
            if not node.mark:
                node.mark = True
            else:
                self._cut(node, p)
                self._cascading_cut(p)

    def _consolidate(self):
        array_size = self.total_nodes * 2
        A = [None] * array_size

        nodes = []
        current = self.min

        while True:
            nodes.append(current)
            current = current.right
            if current == self.min:
                break

        for node in nodes:
            d = node.degree
            while A[d]:
                temp = A[d]
                if node.key > temp.key:
                    node, temp = temp, node

                self._link(temp, node)
                A[d] = None
                d += 1

            A[d] = node

        self.min = None
        for node in A:
            if node:
                if not self.min or node.key < self.min.key:
                    self.min = node

    def _link(self, y, x):
        y.left.right = y.right
        y.right.left = y.left

        y.parent = x
        if not x.child:
            x.child = y
        else:
            y.right = x.child.right
            x.child.right.left = y
            x.child.right = y
            y.left = x.child

        x.degree += 1
        y.mark = False


# ------------------- MENU DRIVER -------------------

fh = FibonacciHeap()

while True:
    print("\n--- FIBONACCI HEAP MENU ---")
    print("1. Insert key")
    print("2. Get minimum")
    print("3. Extract minimum")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = int(input("Enter value to insert: "))
        fh.insert(value)

    elif choice == "2":
        print("Minimum value =", fh.get_min())

    elif choice == "3":
        print("Extracted minimum =", fh.extract_min())

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid Option!")
