#include <iostream>

#include <edb/analysis.h>
#include <edb/binary_search.h>
#include <edb/bubblesort.h>
#include <edb/quicksort.h>
#include <edb/sequencial_search.h>
#include <cli/usage.h>

int main(int argc, char *argv[]) 
{
    std::string program = argv[0];
    if(argc < 2)
    {
        std::cout << "Too few arguments!" << std::endl << std::endl;
        edb::cli::print_usage(program);
        return 1;
    }
    else if(argc > 3)
    {
        std::cout << "Too many arguments!" << std::endl << std::endl;
        edb::cli::print_usage(program);
        return 1;
    }
    
    std::string alg_name = argv[1];
    if (!alg_name.empty() && alg_name[0] == '-') {
        alg_name = alg_name.substr(1);
    }
    
    if(argc == 2)
    {
        if(alg_name != "qs" && alg_name != "bb" && alg_name != "bs" && alg_name != "ss") 
        {
            std::cout << "Invalid argument" << std::endl << std::endl;
            edb::cli::print_usage(program);
        }

        edb::run_analysis(alg_name);
    }
    if(argc == 3) // for ploting the charts
    {
        
    }
  return 0;
} 