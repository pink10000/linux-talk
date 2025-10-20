// multi_core.cpp
#include <iostream>
#include <vector>
#include <thread>

// The worker function that each thread will execute.
void worker() {
    try {
        while (true) {
            volatile double result = 12345.6789 * 98765.4321;
        }
    } catch (...) {}
}

int main() {
    // Detect the number of available hardware cores.
    unsigned int num_cores = std::thread::hardware_concurrency();
    std::cout << "Running multi-threaded C++ task on " << num_cores << " cores... Press Ctrl+C to stop." << std::endl;

    // Create a vector to hold the threads.
    std::vector<std::thread> threads;
    for (unsigned int i = 0; i < num_cores; ++i) {
        threads.emplace_back(worker);
    }

    // Wait for all threads to complete (which they won't, until Ctrl+C).
    for (auto& t : threads) {
        t.join();
    }
    
    return 0;
}
