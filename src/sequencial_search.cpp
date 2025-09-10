#include <edb/sequencial_search.h>

int edb::search::sequencial_search(const std::vector<int>& arr, int key)
{
    for (size_t i = 0; i < arr.size(); ++i)
    {
        if (arr[i] == key) return i;
    }
    
    return -1;
}