#pragma once

#include <iostream>
#include <chrono>
#include <vector>
#include <algorithm>
#include <random>
#include <fstream>
#include <filesystem>
#include <functional>

#include <edb/binary_search.h>
#include <edb/sequencial_search.h>
#include <edb/quicksort.h>
#include <edb/bubblesort.h>


namespace edb
{
    enum class algorithm_type
    {
        BUBBLE,
        QUICK,
        BINARY,
        LINEAR,
    };

    void run_analysis(std::string& algorithm_name);
    void search_analyzer(algorithm_type t,const std::string& filename, const std::function<int(std::vector<int>&, int)>& search_algorithm);
    void sort_analyzer(algorithm_type t, const std::string& filename, const std::function<void(std::vector<int>&, int, int)>& sort_algorithm);
    std::vector<int> vec_setup(int n);
}