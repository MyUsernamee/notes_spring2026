#include <iostream>

struct Node {

    int data;
    Node* prev;
    Node* next;
    // Constructor
    Node(int value) : data(value), prev(nullptr), next(nullptr) { }

} ;

// Doubly linked list class
class DoublyLinkedList {

    private:
        // Head and tail dummy nodes
        Node headDummy;
        Node tailDummy;

        // Private member function to delete a node traversing from the front of the list
        bool deleteFromFront(int value) {
            Node* current = headDummy.next;

            for (; current != &tailDummy; current = current->next) {
                if (current->data == value) {
                    current->prev->next = current->next;
                    current->next->prev = current->prev;
                    delete current;
                    return true;
                }
            }

            return false;
        }

        // Private member function to delete a node from the end of the list
        bool deleteFromEnd(int value) {
            Node* current = tailDummy.prev;

            for (; current != &headDummy; current = current->prev) {
                if (current->data == value) {
                    current->prev->next = current->next;
                    current->next->prev = current->prev;
                    delete current;
                    return true;
                }
            }

            return false;        
        }

        // Private member function to add a node traversing from the front of the list
        void addFromFront(int value) {
            Node* newNode = new Node(value);
            Node* current = headDummy.next;

            if (current == &tailDummy) { // Empty list, add
                headDummy.next = newNode;
                tailDummy.prev = newNode;
                newNode->next = &tailDummy;
                newNode->prev = &headDummy;
                return;
            }

            for (; current != &tailDummy; current = current->next) {
                if (current->data >= value) {
                    newNode->prev = current->prev; 
                    newNode->next = current;
                    current->prev->next = newNode;
                    current->prev = newNode;
                    return;
                }
            }

            // Largest, add to end
            newNode->prev = tailDummy.prev;
            tailDummy.prev = newNode;
        }

        // Private member function to add a node traversing from the end of the list
        void addFromEnd(int value) {
            Node* newNode = new Node(value);
            Node* current = tailDummy.prev;

            if (current == &headDummy) { // Empty list, add
                headDummy.next = newNode;
                tailDummy.prev = newNode;
                newNode->next = &tailDummy;
                newNode->prev = &headDummy;
                return;
            }

            for (; current != &headDummy; current = current->prev) {
                if (current->data <= value) {
                    newNode->prev = current; 
                    newNode->next = current->next;
                    current->next->prev = newNode;
                    current->next = newNode;
                    return;
                }
            }

            // Smallest, add to end
            newNode->next = headDummy.next;
            headDummy.next = newNode;
        }

    public:
        // Constructor
        DoublyLinkedList() : headDummy(0), tailDummy(0) {
            // Connect head and tail dummy nodes
            headDummy.next = &tailDummy;
            tailDummy.prev = &headDummy;
        }

        // Destructor to free memory
        ~DoublyLinkedList() {
            Node* next = headDummy.next;
            for(Node* current = headDummy.next; current != &tailDummy; current = next) {
                next = current->next; 
                delete current;
            }
        }

        // Function to print the elements of the list
        void printList() {
            std::cout << "[";
            for(Node* current = headDummy.next; current->next != nullptr; current = current->next) {
                std::cout << current->data << ", ";
            }
            std::cout << "]" << std::endl;
        }

        //***DO NOT TOUCH ANYTHING BELOW THIS LINE...NOTHING...I MEAN IT!!!***//
        // Public function to delete a node based on value
        bool deleteFromList(int value) {

            // Determine if the value is closer to the head or tail
            int distanceFromHead = value - headDummy.next->data;
            int distanceFromTail = tailDummy.prev->data - value;
            if (distanceFromHead <= distanceFromTail)
                return deleteFromFront(value);
            else
                return deleteFromEnd(value);
        }

        // Public function to add a node to the ordered list
        void addToOrderedList(int value) {

            // Determine if the value is closer to the head or tail
            int distanceFromHead = value - headDummy.next->data;
            int distanceFromTail = tailDummy.prev->data - value;
            if (distanceFromHead <= distanceFromTail)
                addFromFront(value);
            else
                addFromEnd(value);
        }

} ;

int main() {

    // Create a doubly linked list
    DoublyLinkedList myList;
    // Add elements to the ordered list
    myList.addToOrderedList(3);
    myList.addToOrderedList(1);
    myList.addToOrderedList(2);
    myList.addToOrderedList(5);
    myList.addToOrderedList(4);
    // Print the elements of the list
    std::cout << "Here is the current list:" << std::endl;
    myList.printList();
    std::cout << std::endl;
    // Delete a node from the list and print the updated list
    std::cout << "Trying to delete 2 from the list." << std::endl;
    bool deleted = myList.deleteFromList(2);
    if (deleted)
        std::cout << "Successfully deleted value from the list." << std::endl;
    else
        std::cout << "Value not found in the list." << std::endl;
    std::cout << std::endl;
    // Delete a node from the list and print the updated list
    std::cout << "Trying to delete 4 from the list." << std::endl;
    deleted = myList.deleteFromList(4);
    if (deleted)
        std::cout << "Successfully deleted value from the list." << std::endl;
    else
        std::cout << "Value not found in the list." << std::endl;
    std::cout << std::endl;
    // Delete a node from the list and print the updated list
    std::cout << "Trying to delete 4 from the list again.  This should be unsuccessful." << std::endl;
    deleted = myList.deleteFromList(4);
    if (deleted)
        std::cout << "Successfully deleted value from the list." << std::endl;
    else
        std::cout << "Value not found in the list." << std::endl;
    std::cout << std::endl;
    // Print the updated list
    myList.printList();
    std::cout << std::endl;
    // Delete a node from the list and print the updated list
    std::cout << "Trying to delete 5 from the list" << std::endl;
    deleted = myList.deleteFromList(5);
    if (deleted)
        std::cout << "Successfully deleted value from the list." << std::endl;
    else
        std::cout << "Value not found in the list." << std::endl;
    std::cout << std::endl;
    // Print the updated list
    myList.printList();
    std::cout << std::endl;
    // Delete a node from the list and print the updated list
    std::cout << "Trying to delete 1 from the list" << std::endl;
    deleted = myList.deleteFromList(1);
    if (deleted)
        std::cout << "Successfully deleted value from the list." << std::endl;
    else
        std::cout << "Value not found in the list." << std::endl;
    std::cout << std::endl;
    // Print the updated list
    myList.printList();
    std::cout << std::endl;
    return 0;

}

