#include <edb/analysis.h>
#include <cmath>

#define RES_PATH "../results/"



void edb::run_analysis(std::string& algorithm_name)
{
    std::string filename = algorithm_name + "_result.csv";
    try // try to create a dir if it doesn't exists
    {
        std::filesystem::path dir = RES_PATH;;
        if(!std::filesystem::exists(RES_PATH)) std::filesystem::create_directories(dir);
    }
    catch(std::exception& e)
    {
        std::cout << e.what();
        return;
    }

    if(algorithm_name == "bb")
        search_analyzer(algorithm_type::BINARY, std::string(filename), &edb::search::binary_search);
    if(algorithm_name == "ss")
        search_analyzer(algorithm_type::LINEAR, std::string(filename), &edb::search::sequencial_search);
    if(algorithm_name == "qs")
        sort_analyzer(algorithm_type::QUICK, std::string(filename), &edb::sort::quicksort);
    if(algorithm_name == "bs")
        sort_analyzer(algorithm_type::BUBBLE, std::string(filename), &edb::sort::bubblesort);
}

void edb::search_analyzer(edb::algorithm_type t, const std::string& filename, const std::function<int(std::vector<int>&, int)>& search_algorithm)
{
    std::cout << filename;
    int rep; 
    //sets the repetitions to be way longer if is the binary search
    if(t == algorithm_type::BINARY) rep = 2000000;
    else rep = 500;

    std::ofstream res_csv(RES_PATH + std::string("/") + filename);
    res_csv << "n,time_measured" << std::endl;

    for(int n = 10000 ; n < 100001; n*=2)
    {
        auto total_duration = std::chrono::steady_clock::duration::zero();
        std::vector<int> arr = edb::vec_setup(n);
        std::sort(arr.begin(), arr.end());

        for(int j = 0; j < rep; ++j)
        {
            auto start = std::chrono::steady_clock::now();
            search_algorithm(arr, n);
            auto end = std::chrono::steady_clock::now();

            total_duration += (end - start);
        }
        auto average_duration = total_duration / rep;

        std::chrono::duration<double> average_s = average_duration;

        res_csv << n << "," << std::fixed << std::setprecision(10) << average_s.count() << std::endl;
    }
}

void edb::sort_analyzer(edb::algorithm_type t, const std::string& filename, const std::function<void(std::vector<int>&, int, int)>& sort_algorithm)
{
    std::cout << filename << std::endl;
    int rep = 50;

    std::ofstream res_csv(RES_PATH + std::string("/") + filename);
    res_csv << "n,time_measured" << std::endl;

    for(int n = 1000 ; n <=10001; n *= 2)
    {
        auto total_duration = std::chrono::steady_clock::duration::zero();

        for(int j = 0; j < rep; ++j)
        {
            std::vector<int> arr = edb::vec_setup(n);
            auto start = std::chrono::steady_clock::now();
            sort_algorithm(arr, 0, n - 1);
            auto end = std::chrono::steady_clock::now();

            total_duration += (end - start);
        }
        auto average_duration = total_duration / rep;
        std::chrono::duration<double> average_s = average_duration;

        res_csv << n << "," << std::fixed << std::setprecision(10) << average_s.count() << std::endl;
    }
}

std::vector<int> edb::vec_setup(int n)
{
    std::vector<int> random_vec(n);

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distrib(1, n - 1);

    std::generate(random_vec.begin(), random_vec.end(), [&](){ return distrib(gen);});

    return random_vec;
}