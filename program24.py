# Huffman Coding using Greedy Strategy

import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # for priority queue comparison (min-heap based on freq)
    def __lt__(self, other):
        return self.freq < other.freq


# Function to build Huffman Tree
def build_huffman_tree(characters, frequencies):
    heap = [Node(characters[i], frequencies[i]) for i in range(len(characters))]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Extract two nodes with lowest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create new internal node with combined frequency
        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right

        heapq.heappush(heap, new_node)

    return heap[0]


# Function to generate Huffman codes (DFS traversal)
def generate_codes(root, code, huffman_codes):
    if root is None:
        return

    if root.char is not None:  # leaf node
        huffman_codes[root.char] = code

    generate_codes(root.left, code + "0", huffman_codes)
    generate_codes(root.right, code + "1", huffman_codes)


# ----- MAIN PROGRAM -----
print("Huffman Coding using Greedy Strategy\n")

n = int(input("Enter number of characters: "))

chars = []
freqs = []

for i in range(n):
    c = input(f"Enter character {i+1}: ")
    f = int(input(f"Enter frequency of '{c}': "))
    chars.append(c)
    freqs.append(f)

root = build_huffman_tree(chars, freqs)
huffman_codes = {}

generate_codes(root, "", huffman_codes)

print("\nGenerated Huffman Codes:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")
