import java.util.Arrays;
import java.util.Random;

public class SortingBenchmark {

    // Bubble sort O(n^2)
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    // Quick sort O(n log n)
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        return i + 1;
    }

    // Binary search O(log n)
    public static int binarySearch(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) return mid;
            if (arr[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }

    public static void printArray(int[] arr) {
        for (int x : arr) System.out.print(x + " ");
        System.out.println();
    }

    public static void benchmark() {
        int[] sizes = {100, 500, 1000};
        Random rand = new Random();

        for (int size : sizes) {
            int[] arr = new int[size];
            for (int i = 0; i < size; i++) arr[i] = rand.nextInt(1000);

            long start = System.nanoTime();
            bubbleSort(arr.clone());
            long bubbleTime = System.nanoTime() - start;

            arr = new int[size];
            for (int i = 0; i < size; i++) arr[i] = rand.nextInt(1000);

            start = System.nanoTime();
            quickSort(arr, 0, size - 1);
            long quickTime = System.nanoTime() - start;

            System.out.println("Size " + size + ": Bubble=" + bubbleTime/1000 + "us, Quick=" + quickTime/1000 + "us");
        }
    }

    public static void main(String[] args) {
        benchmark();

        int[] arr = {1, 3, 5, 7, 9, 11, 13, 15};
        int idx = binarySearch(arr, 7);
        System.out.println("Found 7 at index: " + idx);
    }
}
