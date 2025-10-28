#include <stdio.h>
#include <stdlib.h>

#define MAX 3   // Max keys in a node
#define MIN 1   // Min keys

struct BTreeNode {
    int data[MAX + 1];
    int count;
    struct BTreeNode *link[MAX + 1];
};

struct BTreeNode *root;

// Create node
struct BTreeNode *createNode(int item, struct BTreeNode *child) {
    struct BTreeNode *newNode;
    newNode = (struct BTreeNode *)malloc(sizeof(struct BTreeNode));
    newNode->data[1] = item;
    newNode->count = 1;
    newNode->link[0] = root;
    newNode->link[1] = child;
    return newNode;
}

// Add value to node
void addValueToNode(int item, int pos, struct BTreeNode *node, struct BTreeNode *child) {
    int j = node->count;
    while (j > pos) {
        node->data[j + 1] = node->data[j];
        node->link[j + 1] = node->link[j];
        j--;
    }
    node->data[j + 1] = item;
    node->link[j + 1] = child;
    node->count++;
}

// Split node
void splitNode(int item, int *pval, int pos, struct BTreeNode *node, struct BTreeNode *child, struct BTreeNode **newNode) {
    int median, j;
    if (pos > MIN)
        median = MIN + 1;
    else
        median = MIN;

    *newNode = (struct BTreeNode *)malloc(sizeof(struct BTreeNode));
    j = median + 1;
    while (j <= MAX) {
        (*newNode)->data[j - median] = node->data[j];
        (*newNode)->link[j - median] = node->link[j];
        j++;
    }
    (*newNode)->count = MAX - median;
    node->count = median;

    if (pos <= MIN)
        addValueToNode(item, pos, node, child);
    else
        addValueToNode(item, pos - median, *newNode, child);

    *pval = node->data[node->count];
    (*newNode)->link[0] = node->link[node->count];
    node->count--;
}

// Set value
int setValueInNode(int item, int *pval, struct BTreeNode *node, struct BTreeNode **child) {
    int pos;
    if (!node) {
        *pval = item;
        *child = NULL;
        return 1;
    }

    if (item < node->data[1])
        pos = 0;
    else {
        for (pos = node->count; (item < node->data[pos] && pos > 1); pos--);
        if (item == node->data[pos])
            return 0;
    }

    if (setValueInNode(item, pval, node->link[pos], child)) {
        if (node->count < MAX)
            addValueToNode(*pval, pos, node, *child);
        else {
            splitNode(*pval, pval, pos, node, *child, child);
            return 1;
        }
    }
    return 0;
}

// Insert
void insert(int item) {
    int flag, i;
    struct BTreeNode *child;

    flag = setValueInNode(item, &i, root, &child);
    if (flag)
        root = createNode(i, child);
}

// Display
void traversal(struct BTreeNode *node) {
    int i;
    if (node) {
        for (i = 0; i < node->count; i++) {
            traversal(node->link[i]);
            printf("%d ", node->data[i + 1]);
        }
        traversal(node->link[i]);
    }
}

// Main
int main() {
    int item, choice;
    while (1) {
        printf("\n1.Insert\n2.Display (Inorder)\n3.Exit\nEnter choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter value: ");
                scanf("%d", &item);
                insert(item);
                break;
            case 2:
                printf("B-Tree elements: ");
                traversal(root);
                printf("\n");
                break;
            case 3:
                exit(0);
            default:
                printf("Invalid choice\n");
        }
    }
}
