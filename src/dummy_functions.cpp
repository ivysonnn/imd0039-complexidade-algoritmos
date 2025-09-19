#include <edb/dummy_functions.h>
#include <edb/analysis.h> 
#include <algorithm>      
#include <vector>

namespace edb {
    namespace analysis {

        // Volatile para evitar que o compilador otimize os loops e os remova.
        volatile int sink;

        // As funções DUMMY não realizam nenhum trabalho útil, servem somente para gastar tempo de processamento de uma maneira
        // que corresponda a uma função de tenha a complexidade da qual queremos
        void dummy_log_n(long long n) 
        {
            std::vector<int> vec(n);
            std::lower_bound(vec.begin(), vec.end(), 0);
        }

        void dummy_n(long long n) 
        {
            // O step foi reduzido para que a função consuma mais tempo e seja uma referência melhor.
            const long long step = 10;
            for (long long i = 0; i < n; i += step)
            {
                sink = i;
            }
        }

        void dummy_n_log_n(long long n) 
        {
            std::vector<int> vec(n); // Evita a geração de números aleatórios, que é custosa.
            std::sort(vec.begin(), vec.end());
        }

        void dummy_n_2(long long n) 
        {
            const long long step = 100; // Step maior para não demorar excessivamente.
            for (long long i = 0; i < n; i += step) 
            {
                for (long long j = 0; j < n; j += step) 
                {
                    sink = i * j;
                }
            }
        }

        void dummy_n_3(long long n) 
        {
            const long long step = 500; // Step ainda maior para O(n³) ser viável.
            for (long long i = 0; i < n; i += step) 
            {
                for (long long j = 0; j < n; j += step) 
                {
                    for (long long k = 0; k < n; k += step) 
                    {
                        sink = i * j * k;
                    }
                }
            }
        }
        
    }
}
