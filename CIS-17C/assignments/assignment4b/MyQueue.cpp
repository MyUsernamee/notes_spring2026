#include "MyQueue.h"
#include <climits>
#include <iostream>

MyQueue::MyQueue() {
    _dummy = {0, nullptr}; 
    _size = 0;
}

MyQueue::MyQueue(const MyQueue& rhs) {
    _dummy = rhs._dummy;
    _size = rhs._size;
}

MyQueue MyQueue::operator=(const MyQueue& rhs) {
    return MyQueue(rhs);
}

void MyQueue::push(int v) {
    _size += 1;
    Node* node = &_dummy;
    while (node->next != nullptr) {
        node = node->next;
    }
    node->next = new Node {v, nullptr};
}

int MyQueue::pop() {
    if (_size == 0)
        return INT_MIN;

    _size -= 1;
    Node *p = _dummy.next;
    int v = p->value;
    _dummy.next = p->next;
    delete p;
    return v;
}

int MyQueue::peek() {
    return _dummy.next->value;
}

int MyQueue::size() {
    return _size;
}

void MyQueue::printQueue() {
    for (Node* current = _dummy.next; current != nullptr; current = current->next) {
        std::cout << current->value << " ";
    }
    std::cout << std::endl;
}

MyQueue::~MyQueue() {
    for (Node* current = _dummy.next; current != nullptr; ) {
        Node* n = current->next;
        delete current;
        current = n;
    }
}

