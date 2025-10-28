#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct Node {
    int key, degree, mark;
    struct Node *parent, *child, *left, *right;
};

struct Node *min = NULL;
int n = 0;

// Create new node
struct Node* createNode(int key) {
    struct Node *node = (struct Node*)malloc(sizeof(struct Node));
    node->key = key;
    node->degree = node->mark = 0;
    node->parent = node->child = NULL;
    node->left = node->right = node;
    return node;
}

// Insert
void insert(int key) {
    struct Node *node = createNode(key);
    if (min == NULL)
        min = node;
    else {
        node->left = min;
        node->right = min->right;
        min->right->left = node;
        min->right = node;
        if (node->key < min->key)
            min = node;
    }
    n++;
}

// Display
void display(struct Node *min) {
    struct Node *temp = min;
    if (temp == NULL) {
        printf("Heap empty\n");
        return;
    }
    printf("Fibonacci Heap elements: ");
    do {
        printf("%d ", temp->key);
        temp = temp->right;
    } while (temp != min);
    printf("\n");
}

// Get minimum
void getMin() {
    if (min)
        printf("Minimum: %d\n", min->key);
    else
        printf("Heap empty\n");
}

int main() {
    int choice, val;
    while (1) {
        printf("\n1.Insert\n2.Display\n3.Get Min\n4.Exit\nEnter choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter value: ");
                scanf("%d", &val);
                insert(val);
                break;
            case 2:
                display(min);
                break;
            case 3:
                getMin();
                break;
            case 4:
                exit(0);
            default:
                printf("Invalid choice\n");
        }
    }
    return 0;
}
