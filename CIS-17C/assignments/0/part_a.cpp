#include <cstddef>
#include <iomanip>
#include <iostream>
#include <cassert>
#include <limits>
#include <string>

#define CURRENCY_PERCISION 2
#define MONTHS_YEAR 12 

const static std::string month_names[MONTHS_YEAR] = {"Janurary", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

long double totalAmount(long double totals[MONTHS_YEAR], size_t size) {
    assert(size <= MONTHS_YEAR);

    long double total = 0.0;
    for (size_t i = 0; i < size; i++)
        total += totals[i];
    
    return total;
}

long double averageValue(long double totals[MONTHS_YEAR], size_t size) {
    return totalAmount(totals, size) / (long double)size;
}

long double largestMonth(long double totals[MONTHS_YEAR], size_t size) {
    assert(size <= MONTHS_YEAR);

    long double max = -std::numeric_limits<long double>::max();
    for (size_t i = 0; i < size; i++)
        max = std::max(totals[i], max);

    return max;
}

long double smallestMonth(long double totals[MONTHS_YEAR], size_t size) {
    assert(size <= MONTHS_YEAR);

    long double min = std::numeric_limits<long double>::max();
    for (size_t i = 0; i < size; i++)
        min = std::min(totals[i], min);

    return min;
}

int main() {

    long double totals[MONTHS_YEAR];

    std::cout << "Please enter the total usage for each month." << std::endl;

    for (int i = 0; i < MONTHS_YEAR; i++) {
        std::cout << month_names[i];
        std::cout << " : $";
        std::cin >> totals[i];

        if (totals[i] < 0.0) {
            i--;
            std::cout << "Please enter a valid monetary value." << std::endl; std::cin.clear(std::ios::badbit);
        }
    }
    std::cout << std::fixed << std::setprecision(CURRENCY_PERCISION) << "The total amount of money spent was $" << totalAmount(totals, MONTHS_YEAR) << std::endl;
    std::cout << std::fixed << std::setprecision(CURRENCY_PERCISION) << "The average amount of money spent per month was $" << averageValue(totals, MONTHS_YEAR) << std::endl;
    std::cout << std::fixed << std::setprecision(CURRENCY_PERCISION) << "The most amount of money spent in a month was $" << largestMonth(totals, MONTHS_YEAR) << std::endl;
    std::cout << std::fixed << std::setprecision(CURRENCY_PERCISION) << "The least amount of money spent in a month was $" << smallestMonth(totals, MONTHS_YEAR) << std::endl;

}
