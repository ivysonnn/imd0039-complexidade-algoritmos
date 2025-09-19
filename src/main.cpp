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
        if (alg_name == "pl") 
        {
            std::string target_alg = argv[2];

            if(target_alg != "qs" && target_alg != "bb" && target_alg != "bs" && target_alg != "ss") 
            {
                std::cout << "Invalid target for plotting: " << target_alg << std::endl << std::endl;
                edb::cli::print_usage(program);
            }

            std::string command = "python3 ../src/plot.py " + target_alg;
            system(command.c_str());
        } else 
        {
            std::cout << "Invalid arguments for plotting." << std::endl << std::endl;
            edb::cli::print_usage(program);
            return 1;
        }
    }
  return 0;
} 