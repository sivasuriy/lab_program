#include <stdio.h>

void activitySelection(int start[], int finish[], int n) {
    int i, j;
    printf("Selected activities are: ");
    
    i = 0; // first activity always selected
    printf("%d ", i + 1);

    for (j = 1; j < n; j++) {
        if (start[j] >= finish[i]) {
            printf("%d ", j + 1);
            i = j;
        }
    }
    printf("\n");
}

int main() {
    int n, i;
    printf("Enter number of activities: ");
    scanf("%d", &n);

    int start[n], finish[n];
    printf("Enter start times: ");
    for (i = 0; i < n; i++)
        scanf("%d", &start[i]);

    printf("Enter finish times: ");
    for (i = 0; i < n; i++)
        scanf("%d", &finish[i]);

    activitySelection(start, finish, n);
    return 0;
}
