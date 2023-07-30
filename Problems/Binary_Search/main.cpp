#include <iostream>


int binarySearch(const int arr[], int size, int key, bool is_left = true) {
    int right = size - 1;
    int left = 0;
    int mid;
    int result = -1;
    while (left <= right) {
        mid = (right + left) / 2;
        if (arr[mid] > key) {
            right = mid - 1;
        } else if (arr[mid] < key) {
            left = mid + 1;
        } else {
            if (is_left) {
                right = mid - 1; // Для левого вхождения.
            } else {
                left = mid + 1; // Для правого вхождения.
            }
            result = mid;
        }
    }
    return result;
}


int main() {
    int size1, size2;
    std::cin >> size1 >> size2;
    int *list1 = new int[size1];
    int *list2 = new int[size2];
    for (int i = 0; i < size1; ++i) {
        std::cin >> list1[i];
    }
    for (int i = 0; i < size2; ++i) {
        std::cin >> list2[i];
    }
    for (int i = 0; i < size2; ++i) {
        int left = binarySearch(list1, size1, list2[i], true);
        int right = binarySearch(list1, size1, list2[i], false);
        if (left == -1) {
            std::cout << left + 1 << std::endl;
        } else {
            std::cout << left + 1 << " " << right + 1 << std::endl;
        }
    }
    return 0;
}


