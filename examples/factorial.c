#include <stdio.h>

// Simple recursive factorial
int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int main() {
    int i;
    for (i = 1; i <= 5; i++) {
        printf("%d! = %d\n", i, factorial(i));
    }
    return 0;
}
