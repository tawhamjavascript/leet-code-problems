#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int numberOfOccur = count(nums.begin(), nums.end(), val);
        int k = nums.size() - numberOfOccur;
        while (1) {
            auto it = find(nums.begin(), nums.end(), val);
            if (it == nums.end()) {
                break;
            }
            nums.erase(it);
        }
        return k;
    }
};


int main() {
    Solution solution;
    vector<int> list = {0,1,2,2,3,0,4,2};
    cout << solution.removeElement(list, 2);
    cout << '\n';
    for(const auto& n: list) {
        cout << n << " ";
    }
}
