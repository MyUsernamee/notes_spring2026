#include "MyStack.h"
#include <iostream>

MyStack::MyStack() {
    _dummy = {0, nullptr}; 
    _size = 0;
}

MyStack::MyStack(const MyStack& rhs) {
    _dummy = rhs._dummy;
    _size = rhs._size;
}

MyStack MyStack::operator=(const MyStack& rhs) {
    return MyStack(rhs);
}

void MyStack::push(int v) {
    _size += 1;
    _dummy.next = new Node {v, _dummy.next};
}

int MyStack::pop() {
    _size -= 1;
    Node *p = _dummy.next;
    int v = p->value;
    _dummy.next = p->next;
    delete p;
    return v;
}

int MyStack::peek() {
    return _dummy.next->value;
}

int MyStack::size() {
    return _size;
}

void MyStack::printStack() {
    for (Node* current = _dummy.next; current != nullptr; current = current->next) {
        std::cout << current->value << " ";
    }
    std::cout << std::endl;
}

MyStack::~MyStack() {
    for (Node* current = _dummy.next; current != nullptr; ) {
        Node* n = current->next;
        delete current;
        current = n;
    }
}

