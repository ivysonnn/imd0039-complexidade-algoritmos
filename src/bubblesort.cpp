#include <edb/bubblesort.h>
#include <utility>

void edb::sort::bubblesort(std::vector<int>& arr, int low, int high)
{
    if (low < 0 || high >= static_cast<int>(arr.size()) || low >= high) return;

    for (int i = low; i <= high; ++i) {
        for (int j = low; j < high - (i - low); ++j) {
            if (arr[j] > arr[j + 1]) std::swap(arr[j], arr[j + 1]);
        }
    }
}