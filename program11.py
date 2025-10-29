import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def delete(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)

    def display(self):
        print("Min Heap:", self.heap)


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, -value)  # push negative to simulate max heap

    def delete(self):
        if not self.heap:
            return None
        return -heapq.heappop(self.heap)

    def display(self):
        # convert back to positive for displaying
        print("Max Heap:", [-x for x in self.heap])


# -------- Main Program --------
if __name__ == "__main__":
    min_heap = MinHeap()
    max_heap = MaxHeap()

    while True:
        print("\n--- HEAP OPERATIONS ---")
        print("1. Insert in Min Heap")
        print("2. Delete from Min Heap")
        print("3. Display Min Heap")
        print("4. Insert in Max Heap")
        print("5. Delete from Max Heap")
        print("6. Display Max Heap")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter value: "))
            min_heap.insert(value)

        elif choice == 2:
            deleted = min_heap.delete()
            print("Deleted:", deleted)

        elif choice == 3:
            min_heap.display()

        elif choice == 4:
            value = int(input("Enter value: "))
            max_heap.insert(value)

        elif choice == 5:
            deleted = max_heap.delete()
            print("Deleted:", deleted)

        elif choice == 6:
            max_heap.display()

        elif choice == 7:
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")
