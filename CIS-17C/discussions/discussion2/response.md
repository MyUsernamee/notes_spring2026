There are a number of reasons not to rely on the default C++ constructor. One of the largest sources of security issues and bugs in software is attempting to use memory with unspecified states. In the case of the default constructor, it will not initialize any member variables that don't have a default value. This can lead to undefined behavior. In the best case scenario, this is just a crash, in the worst case, it can provide attackers a "golden free access pass" to your program. Having predictable state also makes your code easier to maintain and less prone to errors in different environments (i.e. which compiler is used to compile your program, or what os it is built on), or updates. To ensure neither of these happens, as a programmer you should always define a constructor, and initialize every member variable explicitly. On every class you write, it should be accompanied with a default constructor. In the default constructor, you should make sure that every member variable has an assignment in every possible code path in this constructor.

Here is an example of a C++ class without a default constructor, as well as a sample run to show what happens if you don't define one.

```cpp
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
```

When run, the program instantly crashes with a segmentation fault: 

```bash
[1]    2188236 segmentation fault (core dumped)  ./a.out
```

Which for us is great news because, in the right set of circumstances, this can be use to allow attackers to read memory they are not supposed to.
