#include <edb/quicksort.h>

namespace //blank namespace to make partition "private"
{
    int partition(std::vector<int>& arr, int low, int high)
    {
        int pivot = arr[(low + high) / 2];
        int i = low - 1;
        int j = high + 1;
        while (true) {
            do { ++i; } while (arr[i] < pivot);
            do { --j; } while (arr[j] > pivot);
            if (i >= j) return j;
            std::swap(arr[i], arr[j]);
        }
    }
}

void edb::sort::quicksort(std::vector<int>& arr, int low, int high)
{
    if(low < high)
    {
        int pi = partition(arr, low, high);
        edb::sort::quicksort(arr, low, pi);
        edb::sort::quicksort(arr, pi + 1, high);
    }
}