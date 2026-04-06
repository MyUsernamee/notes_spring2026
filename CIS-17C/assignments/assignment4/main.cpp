#include "MyStack.h"
#include <iostream>

using namespace std;

int main () {
    MyStack S;

    S.push(1);
    S.push(2);
    S.push(3);
    S.push(5);
    S.push(6);

    cout << "Testing push()" << endl;
    S.printStack();
}
