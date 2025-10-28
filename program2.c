#include <stdio.h>

int main() {
    int n, i;
    long a = 0, b = 1, c;

    printf("Enter number of terms: ");
    scanf("%d", &n);

    printf("Fibonacci Series: %ld %ld ", a, b);

    for (i = 3; i <= n; i++) {
        c = a + b;
        printf("%ld ", c);
        a = b;
        b = c;
    }

    printf("\n");
    return 0;
}
