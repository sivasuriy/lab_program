#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX 100

int heap[MAX];
int size = 0;

// swap
void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

// insert
void insert(int val) {
    heap[++size] = val;
    int i = size;
    while (i > 1 && heap[i / 2] > heap[i]) {
        swap(&heap[i], &heap[i / 2]);
        i /= 2;
    }
}

// heapify down
void heapify(int i) {
    int smallest = i, left = 2 * i, right = 2 * i + 1;
    if (left <= size && heap[left] < heap[smallest])
        smallest = left;
    if (right <= size && heap[right] < heap[smallest])
        smallest = right;
    if (smallest != i) {
        swap(&heap[i], &heap[smallest]);
        heapify(smallest);
    }
}

// decrease key
void decreaseKey(int i, int newVal) {
    heap[i] = newVal;
    while (i > 1 && heap[i / 2] > heap[i]) {
        swap(&heap[i], &heap[i / 2]);
        i /= 2;
    }
}

// extract minimum
int extractMin() {
    if (size == 0) return INT_MIN;
    int root = heap[1];
    heap[1] = heap[size--];
    heapify(1);
    return root;
}

// delete key
void deleteKey(int i) {
    decreaseKey(i, INT_MIN);
    extractMin();
}

// display
void display() {
    if (size == 0) {
        printf("Heap empty\n");
        return;
    }
    printf("Heap elements: ");
    for (int i = 1; i <= size; i++)
        printf("%d ", heap[i]);
    printf("\n");
}

int main() {
    int ch, val, pos;
    while (1) {
        printf("\n1.Insert\n2.Display\n3.Decrease Key\n4.Delete Key\n5.Exit\nEnter choice: ");
        scanf("%d", &ch);
        switch (ch) {
            case 1:
                printf("Enter value: ");
                scanf("%d", &val);
                insert(val);
                break;
            case 2:
                display();
                break;
            case 3:
                printf("Enter index and new value: ");
                scanf("%d%d", &pos, &val);
                decreaseKey(pos, val);
                break;
            case 4:
                printf("Enter index to delete: ");
                scanf("%d", &pos);
                deleteKey(pos);
                break;
            case 5:
                exit(0);
            default:
                printf("Invalid choice\n");
        }
    }
}