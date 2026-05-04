#include <stdio.h>

int main() {
    int a = 7;
    int m = 32767;
    int* x = (int*)(0x3F01);
    int q = m / a;
    int r = m % a;
    int i = 0;
    while (i < 20) {
        *x = a * (*x % q) - r * (*x / q);
        if (*x < 0) {
            *x = *x + m;
        }
        i ++;
    }
    printf("%i\n", *x);
    return 0;
}
