#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> map;
        for(const auto& num : nums) {
            if (map.count(num) > 0) {
                return true;
            }
            map[num] = 0;
        }
        return false;
    }
};

int main() {
    Solution solution;
    vector<int> teste = {1,1,1,3,3,4,3,2,4,2};
    cout << solution.containsDuplicate(teste);


}
