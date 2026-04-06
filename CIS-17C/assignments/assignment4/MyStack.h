//
//  MyStack.h
//
//  This contains all of the header files for the MyStack class.


#ifndef MyStack_h
#define MyStack_h

#include "Node.h"

using namespace std;

class MyStack {
    private:
        Node _dummy;
        unsigned int _size;
    public:
        MyStack();
        MyStack(const MyStack& rhs);
        MyStack operator=(const MyStack& rhs);
        void push(int v);
        int pop();
        int peek();
        int size();
        void printStack();
        ~MyStack();
};

#endif /* MyStack_h */
