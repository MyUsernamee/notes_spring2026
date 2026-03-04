#include <cstring>
#include <iostream>

class MyAmazingDatabase {
    /// A simple database that is _100%_ secure with no crashes every :D. (sarcasm)

private:
    char* super_secret_data; // Here we use a char* (c string) to more clearly demonstrate how not initializing this member variable can cause some really bad issues.
    char* secret_password;

public:
    // MyAmazingDatabase() {
    //     super_secret_data = (char*)"";
    //     secret_password = (char*)"MYINCREDIBLEPASWORD";
    // }
    // No explicit constructor, this will lead to undefined behavior.

    /// Check if `password` is valid.
    bool check_password(char* password) {
        return strcmp(password, secret_password) == 0;
    }

    void set_data(char* password, char* new_data) {
        if(!check_password(password))
            return;
        super_secret_data = new_data; // There is a memory-leak here, but we will ignore. Also this is just insecure period, but it is to demonstrate a point.
    }

    void print_super_secret_data(char* password) {
        if (!check_password(password))
            return; // Sorry, no data for you.

        std::cout << super_secret_data << std::endl;
    }
};

int main() {
    // Create "database"
    MyAmazingDatabase db = MyAmazingDatabase();

    // db.set_data("MYINCREDIBLEPASWORD", "Some super secret data.");
    // Our library user doesn't set data D:.
    db.print_super_secret_data("MYINCREDIBLEPASWORD");
    // Then tries to access it; Because we added a default constructor, this will just print an empty string.

    return 0;
}
