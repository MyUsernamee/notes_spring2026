#include <iostream>
#include <fstream>

void readPrices(std::ifstream& file, int prices[15]) {
    std::string line;
    file >> line;
    for (int i = 0; !file.fail(); i++) {
        prices[i] = std::stoi(line.substr(1));
        file >> line;
    }
}

void displayPrices(int* prices, size_t size) {
    for (int i = 0; i < size; i++) {
        std::cout << "$" << prices[i] << std::endl;
    }
}

int main() {

    std::ifstream price_file = std::ifstream("./prices.txt");
    int prices[15];
    readPrices(price_file, prices);
    std::cout << "The prices for the 15 rows are:" << std::endl;
    displayPrices(prices, 15);
    
    return 0;
}
