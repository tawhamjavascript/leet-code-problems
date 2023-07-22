#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        for (int i = 0; i < nums.size() - 1; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int left = i + 1;
            int right = nums.size() - 1;
            while (left < right) {
                int value = nums[i] + nums[left] + nums[right];
                if (value > 0) {
                    right --;
                }
                else if (value < 0) {
                    left ++;
                }
                else {
                    result.push_back({nums[i], nums[left], nums[right]});
                    left ++;
                    while(nums[left] == nums[left - 1] && left < right) {
                        left ++;
                    }
                }
            }
        }
        return result;
    }
};



int main() {
    Solution solution;
    vector<int> teste = {-1, -1, -1, 2, 2};
    vector<vector<int>> result = solution.threeSum(teste);
    for(const auto& v: result) {
        for(const auto& n: v) {
            cout << n << " ";
        }
        cout << '\n';
    }
}
