#include <edb/binary_search.h>

int edb::search::binary_search(const std::vector<int>& arr, int key)
{
  int start = 0;
  int end = (int)arr.size() - 1;
  while(start <= end)
  {
    int middle = start + (end - start) / 2;

    if(arr[middle] == key) return middle;
    if(arr[middle] < key ) start = middle + 1; 
    if(arr[middle] > key) end = middle - 1;
  }

  return -1;
}