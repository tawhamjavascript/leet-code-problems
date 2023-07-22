#include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> items(nums.begin(), nums.end());
        int longest = 0;
        for(const auto& num: nums) {
            if(items.count(num - 1) == 0) {
                int length = 0;
                while(items.count(length + num) > 0) {
                    length ++;
                }
                longest = max(longest, length);
            }
        }
        return longest;
    }
};


int main() {

}
