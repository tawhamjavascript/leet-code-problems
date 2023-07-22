#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> pilha;
        for(const auto& str : s) {
            if (str == '(' || str == '{' || str == '[') {
                pilha.push(str);
            }
            else {
                if (pilha.empty()) {
                    return false;
                }
                if(str == ')' && pilha.top() == '(') {
                    pilha.pop();
                }
                else if(str == '}' && pilha.top() == '{') {
                    pilha.pop();
                }
                else if (str == ']' && pilha.top() == '[') {
                    pilha.pop();
                }
                else {
                    return false;
                }
            }
        }
        return pilha.empty();
    }
};

int main() {
    Solution solution;
    cout << solution.isValid("()");
}
