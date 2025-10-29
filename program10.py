# program10.py
# Min Heap – Insert, Decrease Key, Delete, Extract Min

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert(self, key):
        self.heap.append(key)
        index = len(self.heap) - 1

        # Fix heap order
        while index != 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = \
                self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def decrease_key(self, index, new_value):
        self.heap[index] = new_value

        # Move up until heap property is satisfied
        while index != 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = \
                self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def extract_min(self):
        if len(self.heap) == 0:
            return None

        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        self.min_heapify(0)
        return root

    def delete(self, index):
        # decrease key to -∞ then extract min
        self.decrease_key(index, float("-inf"))
        self.extract_min()

    def min_heapify(self, i):
        smallest = i
        l = self.left(i)
        r = self.right(i)

        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < len(self.heap) and self.heap[r]()
