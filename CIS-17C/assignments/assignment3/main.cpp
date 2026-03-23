#include <iostream>

using namespace std;

struct Node{
    int value;
    Node *next;
};

class LinkedList{
    private:
        Node *m_head;
        Node *m_tail;
        unsigned int m_size;

        void copy_other(const LinkedList &other) {
            m_head = new Node{other.m_head->value, nullptr};
            m_tail = m_head;
            m_size = other.m_size;
            for (Node* node = other.m_head->next; node != nullptr; node=node->next) {
                m_tail->next = new Node{node->value}; 
                m_tail = m_tail->next;
            }

        }

    public:
        LinkedList(){
            m_head = nullptr; // List is empty by default.
            m_tail = nullptr; // Possible undefined behavior. Assume user of our code doesn't do this :(
            m_size = 0;
        }
        LinkedList(const LinkedList& first){
            copy_other(first);
        }
        ~LinkedList(){
            for (Node* node = m_head; node != nullptr;) {
                Node* next_node = node->next; 
                delete node;
                node = next_node;
            }
        }
        LinkedList operator=(const LinkedList& src){
            copy_other(src);
            return *this;
        }
        int size(){
            return (int)m_size; // Unsigned to signed int conversion :(
        }

        void addToFront(int v){
            Node* new_node = new Node{v, m_head};
            m_head = new_node;
            m_size += 1;
        }
        void addToRear(int v){
            Node* new_node = new Node{v, nullptr};
            m_size += 1;

            if (m_tail == nullptr) {
                m_head = new_node;
                m_tail = new_node;
                return;
            }

            m_tail->next = new_node;
            m_tail = new_node;
        }
        void deleteItem(int v){
            for (Node *node = m_head, *last = nullptr; node != nullptr; node=node->next) {
                if (node->value != v) {
                    last = node;
                    continue;
                }

                if (last != nullptr && node->next != nullptr) 
                    last->next = node->next->next;
                else if (last != nullptr) {
                    last->next = nullptr;
                    m_tail = last;
                }
                else {
                    m_head = node->next;
                }

                delete node;
                m_size -= 1;

                break; // All done :)
            }
        }

        void swapList(LinkedList& other){ // I removed the const here
                                          // We are modifiying the other LinkedList; As such,
                                          // the const is misleading as we are modifiying other. 
                                          // If it were const, it would be impossible to swap
                                          // the lists if the other was empty without storing
                                          // extra data.
            Node* tmp_head = other.m_head;
            Node* tmp_tail = other.m_tail;

            other.m_head = m_head;
            other.m_tail = m_tail;
        
            m_head = tmp_head;
            m_tail = tmp_tail;
        }

        void printItems(){
            if (m_size == 0)
                return; 

            for (Node* node = m_head; node != nullptr; node=node->next) {
                    std::cout << node->value << " ";
            }
        }

};

int main() {
    //LEAVE MAIN ALONE PLEASE!!!  <--NO REALLY...I MEAN IT!!!
    //Testing the addToRear function
    LinkedList L;
    L.addToRear(1);
    L.addToRear(2);
    L.addToRear(3);
    L.addToRear(5);
    L.addToRear(6);
    cout << "Testing addToRear()" << endl;
    L.printItems();
    cout << endl;
    cout << endl;
    //Testing the addToFront function
    L.addToFront(7);
    L.addToFront(8);
    cout << "Testing addToFront()" << endl;
    L.printItems();
    cout << endl;
    cout << endl;
    //Testing the size function
    cout << "The size of the list L is " << L.size() << endl;
    cout << endl;
    cout << endl;
    //Testing the copy constructor
    LinkedList LL(L);
    cout << "Testing the copy constructor" << endl;
    LL.printItems();
    cout << endl;
    cout << endl;
    //Testing the swapList function
    LinkedList LLL;
    LLL.addToFront(20);
    LLL.addToFront(30);
    LLL.addToFront(40);
    LLL.addToFront(50);
    LL.swapList(LLL);
    cout << "Testing swapList()" << endl;
    cout << "This is the output of LL" << endl;
    LL.printItems();
    cout << endl;
    cout << "This is the output of LLL" << endl;
    LLL.printItems();
    cout << endl;
    cout << endl;
    //Testing the assignment "=" operator
    L = LL = LLL;
    cout << "Testing the assignment \"=\" operator" << endl;
    cout << "This is the output of L" << endl;
    L.printItems();
    cout << endl;
    cout << "This is the output of LL" << endl;
    LL.printItems();
    cout << endl;
    cout << "This is the output of LLL" << endl;
    LLL.printItems();
    cout << endl;
    cout << endl;
    //Testing the deleteItem function
    LLL.deleteItem(3);
    LLL.deleteItem(5);
    cout << "Testing deleteItem()" << endl;
    LLL.printItems();
    cout << endl;
    cout << endl;
    //Testing the remainder of the deleteItem function
    LLL.deleteItem(1);
    LLL.deleteItem(2);
    LLL.deleteItem(6);
    LLL.deleteItem(7);
    LLL.deleteItem(8);
    cout << "This list should be empty" << endl;
    LLL.printItems();
    cout << "Yep...the list was empty" << endl;
    cout << endl;
    cout << endl;
    //Testing the destructor operator
    cout << "Testing the destructor" << endl;
    L.~LinkedList();
    cout << "Destructor called.  This program still runs." << endl;
}
