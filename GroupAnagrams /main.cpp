#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        for(auto& s: strs) {
            string x = s;
            sort(x.begin(), x.end());
            map[x].push_back(s);
        }
        vector<vector<string>> result;
        result.reserve(map.size());
        for(const auto& [key, value]: map) {
            result.push_back(value);
        }
        return result;
    }
};

int main() {
    Solution solution;
    vector<string> resul = {"eat","tea","tan","ate","nat","bat"};
    cout << solution.groupAnagrams(resul);
}
