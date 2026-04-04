#include <iostream>
#include "MyQueue.h"

using namespace std;

int main () {
    MyQueue S;
    S.push(1);
    S.push(2);
    S.push(3);
    S.push(5);
    S.push(6);
    cout << "Testing push()" << endl;
    S.printQueue();
}
