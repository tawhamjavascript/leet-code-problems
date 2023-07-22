#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result(nums.size(), 1);
        int prefix = 1;
        for(int i = 0; i < nums.size(); i++) {
            result[i] = prefix;
            prefix *= nums[i];
        }

        int posfix = 1;

        for(int i = nums.size() - 1; i > -1; i--) {
            result[i] *= posfix;
            posfix *= nums[i];


        }
        return result;

    }
};

int main() {
    Solution solution;
    vector<int> test = {1,2,3,4};
    solution.productExceptSelf(test);

}
