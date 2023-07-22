#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int, int> map;
        for(int i = 0; i < nums.size(); i++) {
            int result = target - nums[i];
            if (map.count(result)) {
                cout << "encontrando o resultado" << '\n';

                return {map[result], i};
            }
            map[nums[i]] = i;
        }

        return {};
    }
};


int main () {
    Solution solution;
    vector<int> list = {2,7,11,15};
    vector<int> result = solution.twoSum(list, 9);
    for(const auto& index : result) {
        cout << index << '\n';
    }

}