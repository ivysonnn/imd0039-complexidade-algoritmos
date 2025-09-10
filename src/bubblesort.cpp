#include <bubblesort.h>

void edb::sort::bubblesort(std::vector<int>& arr){
    int tamanho = arr.size();
    for(int i = 0; i < tamanho - 1; i++){
        for(int j = 0; j < tamanho - 1 - i; j++){
            
            if (arr[j] > arr[j+1]) std::swap(arr[j], arr[j+1]);
        }     
    }
}