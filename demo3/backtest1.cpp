// single_core.cpp
#include <iostream>

int main() {
    std::cout << "Running single-threaded C++ task... Press Ctrl+C to stop." << std::endl;
    try {
        while (true) {
            // Perform a meaningless but CPU-intensive calculation.
            volatile double result = 12345.6789 * 98765.4321;
        }
    } catch (...) {} // Catch Ctrl+C signal
    
    std::cout << "\nStopping." << std::endl;
    return 0;
}
