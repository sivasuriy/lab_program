# program7.py
# Red-Black Tree Implementation (Insert + Inorder Traversal)

class Node:
    def __init__(self, data):
        self.data = data
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NULL = Node(None)
        self.NULL.color = "BLACK"
        self.root = self.NULL

    def insert(self, key):
        new_node = Node(key)
        new_node.left = self.NULL
        new_node.right = self.NULL

        parent = None
        current = self.root

        while current != self.NULL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = "BLACK"
            return

        if new_node.parent.parent is None:
            return

        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node.parent.color == "RED":
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left

                if uncle.color == "RED":
                    uncle.color = "BLACK"
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.rotate_left(node.parent.parent)

            else:
                uncle = node.parent.parent.right

                if uncle.color == "RED":
                    uncle.color = "BLACK"
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.rotate_right(node.parent.parent)

            if node == self.root:
                break

        self.root.color = "BLACK"

    def rotate_left(self, node):
        temp = node.right
        node.right = temp.left

        if temp.left != self.NULL:
            temp.left.parent = node

        temp.parent = node.parent

        if node.parent is None:
            self.root = temp
        elif node == node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp

        temp.left = node
        node.parent = temp

    def rotate_right(self, node):
        temp = node.left
        node.left = temp.right

        if temp.right != self.NULL:
            temp.right.parent = node

        temp.parent = node.parent

        if node.parent is None:
            self.root = temp
        elif node == node.parent.right:
            node.parent.right = temp
        else:
            node.parent.left = temp

        temp.right = node
        node.parent = temp

    def inorder(self, node):
        if node != self.NULL:
            self.inorder(node.left)
            print(f"{node.data} ({node.color})", end="  ")
            self.inorder(node.right)


# ---------------------- Menu driven program ----------------------

tree = RedBlackTree()

while True:
    print("\n--- RED BLACK TREE MENU ---")
    print("1. Insert")
    print("2. Inorder Traversal")
    print("3. Exit")

    ch = input("Enter option: ")

    if ch == '1':
        val = int(input("Enter value to insert: "))
        tree.insert(val)
    elif ch == '2':
        print("Inorder Traversal (value(color)):")
        tree.inorder(tree.root)
        print()
    elif ch == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
