#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
using namespace std;
using namespace chrono;

// Bubble sort - O(n^2)
void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// Quick sort - O(n log n)
void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr[i], arr[j]);
            }
        }
        swap(arr[i + 1], arr[high]);
        int pi = i + 1;
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Binary search - O(log n)
int binarySearch(const vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

// Print array
void printArray(const vector<int>& arr) {
    for (int x : arr) cout << x << " ";
    cout << endl;
}

// Benchmark sorting
void benchmark() {
    vector<int> sizes = {100, 500, 1000};
    for (int size : sizes) {
        vector<int> arr(size);
        for (int i = 0; i < size; i++) arr[i] = rand() % 1000;

        auto start = high_resolution_clock::now();
        bubbleSort(arr);
        auto bubbleTime = duration_cast<microseconds>(high_resolution_clock::now() - start).count();

        arr = vector<int>(size);
        for (int i = 0; i < size; i++) arr[i] = rand() % 1000;

        start = high_resolution_clock::now();
        quickSort(arr, 0, size - 1);
        auto quickTime = duration_cast<microseconds>(high_resolution_clock::now() - start).count();

        cout << "Size " << size << ": Bubble=" << bubbleTime << "us, Quick=" << quickTime << "us" << endl;
    }
}

int main() {
    benchmark();

    vector<int> arr = {1, 3, 5, 7, 9, 11, 13, 15};
    int idx = binarySearch(arr, 7);
    cout << "Found 7 at index: " << idx << endl;

    return 0;
}
