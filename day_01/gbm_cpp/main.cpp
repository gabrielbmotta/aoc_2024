#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <unordered_map>

using std::vector, std::tuple, std::unordered_map;

tuple<vector<int>, vector<int>> getLists(const char* file_path)
{
    std::ifstream input_file(file_path);
    vector<int> v1, v2;
    
    if(input_file.is_open()){
        int input1, input2; 
        while(input_file >> input1 >> input2){
            v1.push_back(input1);
            v2.push_back(input2);
        }
    } else{
        std::cerr << "No input file found.\n";
        exit(1);
    }
    return {v1, v2};
}

int listDiffs(vector<int> l1, vector<int> l2)
{
    int sum = 0;
    //we assume they are the same size
    for(auto i = 0; i < l1.size(); ++i){
        sum += std::abs(l1[i] - l2[i]);
    }
    return sum;
}

unordered_map<int, int> listFrequencyMap(vector<int> l)
{
    unordered_map<int, int> m;
    for (auto& i : l){
        if(m.contains(i)){
            ++m[i];
        } else{
            m[i] = 1;
        }
    }

    return m;
}

int similarityScore(vector<int> l1, vector<int> l2)
{
    auto m = listFrequencyMap(l2);
    int sum = 0;
    for(auto& i : l1){
        if(m.contains(i)){
            sum += i * m[i];
        }
    }
    return sum;
}

int main(int argc, char* argv[])
{
    auto [v1, v2] = getLists("input.txt");
   
    std::sort(v1.begin(), v1.end());
    std::sort(v2.begin(), v2.end());

    std::cout << "Part 1: " << listDiffs(v1, v2) << "\n";
    std::cout << "Part 2: " << similarityScore(v1, v2) << "\n";

    return 0;
}
