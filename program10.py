# Program 10: Min Heap with Insert, Decrease Key and Delete Element

class MinHeap:
    def __init__(self):
        self.heap = []

    # Function to insert a value into the heap
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    # Function to decrease the key at a given index
    def decrease_key(self, index, new_value):
        if index < 0 or index >= len(self.heap):
            print("Invalid index")
            return

        if new_value > self.heap[index]:
            print("New key is greater than current key, cannot decrease.")
            return

        self.heap[index] = new_value
        self._heapify_up(index)
        print(f"Key decreased at index {index} to {new_value}")

    # Function to delete element at given index
    def delete(self, index):
        if index < 0 or index >= len(self.heap):
            print("Invalid index")
            return
        
        print(f"Deleting element {self.heap[index]} at index {index}")
        self.decrease_key(index, float('-inf'))
        self.extract_min()

    # Function to remove the minimum element
    def extract_min(self):
        if not self.heap:
            print("Heap is empty.")
            return None
        
        minimum = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return minimum

    # Heapify upward (Fix on insert or decrease key)
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    # Heapify downward (Fix after delete / extract min)
    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

# -----------------------
# MAIN PROGRAM
# -----------------------

heap = MinHeap()

while True:
    print("\n--- Min Heap Operations ---")
    print("1. Insert")
    print("2. Decrease Key")
    print("3. Delete Element")
    print("4. Extract Min")
    print("5. Display Heap")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to insert: "))
        heap.insert(value)

    elif choice == 2:
        index = int(input("Enter index to decrease: "))
        new_value = int(input("Enter new value: "))
        heap.decrease_key(index, new_value)

    elif choice == 3:
        index = int(input("Enter index to delete: "))
        heap.delete(index)

    elif choice == 4:
        print("Extracted Min:", heap.extract_min())

    elif choice == 5:
        print("Current Heap:", heap.heap)

    elif choice == 6:
        print("Exiting...")
        break
        
    else:
        print("Invalid choice! Try again.")
