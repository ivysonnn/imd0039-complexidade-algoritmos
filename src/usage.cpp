#include <cli/usage.h>

void edb::cli::print_usage(std::string& program_name)
{
    std::cout << "Usage: " << program_name << " [option]" << std::endl;
    std::cout << "Options:" << std::endl;
    std::cout << "  -h                   Show this help message" << std::endl;
    std::cout << "  -qs                  Runs analysis to the Quicksort algorithm." << std::endl;
    std::cout << "  -bs                  Runs analysis to the Binary Search algorithm." << std::endl;
    std::cout << "  -pl <target>         Plots the data for a target ('qs' ou 'bs')." << std::endl;
}