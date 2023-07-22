#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> map;
        for(const auto& c: s) {
            map[c]++;
        }

        for(const auto& c: t) {
            map[c]--;
        }

        for(const auto& x: map) {
            if(x.second != 0) {
                return false;
            }
        }
        return true;
    }
};
int main() {
    Solution solution;
    cout << solution.isAnagram("a", "ab");

}
