"""Sorting algorithms comparison module."""
import random
import time

def bubble_sort(arr):
    """O(n^2) bubble sort implementation."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    """O(n log n) quick sort implementation."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def binary_search(arr, target):
    """O(log n) binary search."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def benchmark():
    """Compare sorting performance."""
    sizes = [100, 500, 1000]
    for size in sizes:
        arr = [random.randint(0, 1000) for _ in range(size)]

        start = time.time()
        bubble_sort(arr.copy())
        bubble_time = time.time() - start

        start = time.time()
        quick_sort(arr.copy())
        quick_time = time.time() - start

        print(f"Size {size}: Bubble={bubble_time:.4f}s, Quick={quick_time:.4f}s")

def main():
    benchmark()

    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    idx = binary_search(arr, 7)
    print(f"Found 7 at index: {idx}")

if __name__ == '__main__':
    main()
