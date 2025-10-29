# program6.py
# Tree Traversals: Inorder, Preorder, Postorder (Binary Tree)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def insert(root, key):
    """Insert nodes just to build a binary tree for traversal."""
    if root is None:
        return Node(key)
    else:
        if key < root.data:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def inorder(root):
    """Left → Root → Right"""
    if root:
        inorder(root.left)
        print(root.data, end=" ")

def preorder(root):
    """Root → Left → Right"""
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    """Left → Right → Root"""
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

# ---------- Menu Driven Program ----------
root = None

while True:
    print("\n--- TREE OPERATIONS ---")
    print("1. Insert")
    print("2. Inorder Traversal")
    print("3. Preorder Traversal")
    print("4. Postorder Traversal")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        element = int(input("Enter value to insert: "))
        root = insert(root, element)
    elif choice == '2':
        print("Inorder Traversal: ", end="")
        inorder(root)
        print()
    elif choice == '3':
        print("Preorder Traversal: ", end="")
        preorder(root)
        print()
    elif choice == '4':
        print("Postorder Traversal: ", end="")
        postorder(root)
        print()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid option! Try again.")
