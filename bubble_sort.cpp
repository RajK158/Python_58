#include <iostream>
#include <cstdlib>  // for rand()
#include <ctime>    // for time()
using namespace std;

int main() {
    int arr[10];              // create an array of 10 ints
    int *p = arr;             // pointer to the array
    srand(time(0));           // seed for random number

    // Fill array with random numbers
    for (int i = 0; i < 10; i++) {
        *(p + i) = rand() % 100;   // values from 0 to 99
    }

    // Output original array (only this line uses [])
    cout << "Original array: ";
    for (int i = 0; i < 10; i++) {
        cout << *(p + i) << " ";
    }
    cout << endl;

    // Bubble sort (using pointer arithmetic, no [])
    for (int i = 0; i < 10 - 1; i++) {
        for (int j = 0; j < 10 - i - 1; j++) {
            if (*(p + j) > *(p + j + 1)) {
                // swap using temp
                int temp = *(p + j);
                *(p + j) = *(p + j + 1);
                *(p + j + 1) = temp;
            }
        }
    }

    // Output sorted array
    cout << "Sorted array: ";
    for (int i = 0; i < 10; i++) {
        cout << *(p + i) << " ";
    }
    cout << endl;

    return 0;
}
