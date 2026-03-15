#include <iostream>

using namespace std;

void deleteS(char* str) {
    while (*str != '\0') {
        if (*str == 'S' || *str == 's') {
            for (char* str_p = str + 1; *(str_p-1) != '\0'; str_p ++)
                *(str_p - 1) = *str_p; // Remove S by shifting string back one.
            str--;
        }
        str++;
    }
}

int main() {
    char test_str[] = "Supercalifragilisticexpialidocious";
    deleteS(test_str);
    printf("%s", test_str);
}
