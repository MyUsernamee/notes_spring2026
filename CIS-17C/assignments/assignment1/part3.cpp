#include <iostream>

using namespace std;

// return true if two C strings are equal
bool match(char* str1, char* str2) {
    while (str1 != 0 && str2 != 0) { // zero bytes at ends
        if (str1 != str2) // compare corresponding chars
            return false;
        str1++; // advance to the next character
        str2++;
    }
    return str1 == str2; // both ended at same time?
}

int main(){
    char a[10] = "pointy";
    char b[10] = "pointless";
    if (match(a,b))
        cout << "They're the same!\n";
    else
        cout << "They’re different!\n";
    return 0;
}

