#include <iostream>
#include<bits/stdc++.h>

using namespace std;



class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        vector<vector<int>> index_map(nums.size() + 1);
        vector<int> result;

        for(const auto& num: nums) {
            map[num]++;
        }

        for(const auto& [key, val]: map) {
            index_map[val].push_back(key);

        }

        for(int i = index_map.size() - 1; i > -1; i--) {
            auto temp = index_map[i];
            if (!temp.empty()) {
                result.insert(result.end(), temp.begin(), temp.end());

            }
            if (result.size() == k) {
                return result;
            }

        }

        return result;
    }
};


int main() {
    Solution solution;
    vector<int> test = {3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6};

    vector<int> resul = solution.topKFrequent(test, 1);
    for(auto n: resul) {
        cout << n << " ";
    }
}
