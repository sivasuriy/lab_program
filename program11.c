#include <stdio.h>
#include <stdlib.h>

#define MAX 100
int heap[MAX], size = 0;

// swap
void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

// Min-Heap insert
void insertMin(int val) {
    heap[++size] = val;
    int i = size;
    while (i > 1 && heap[i / 2] > heap[i]) {
        swap(&heap[i], &heap[i / 2]);
        i /= 2;
    }
}

// Max-Heap insert
void insertMax(int val) {
    heap[++size] = val;
    int i = size;
    while (i > 1 && heap[i / 2] < heap[i]) {
        swap(&heap[i], &heap[i / 2]);
        i /= 2;
    }
}

// display
void display() {
    if (size == 0) {
        printf("Heap empty\n");
        return;
    }
    for (int i = 1; i <= size; i++)
        printf("%d ", heap[i]);
    printf("\n");
}

int main() {
    int ch, val, type;
    while (1) {
        printf("\n1.Insert\n2.Display\n3.Exit\nEnter choice: ");
        scanf("%d", &ch);
        switch (ch) {
            case 1:
                printf("Enter 1 for Min-Heap, 2 for Max-Heap: ");
                scanf("%d", &type);
                printf("Enter value: ");
                scanf("%d", &val);
                size = 0; // reset for new heap type
                if (type == 1)
                    insertMin(val);
                else
                    insertMax(val);
                break;
            case 2:
                printf("Heap elements: ");
                display();
                break;
            case 3:
                exit(0);
            default:
                printf("Invalid choice\n");
        }
    }
}
