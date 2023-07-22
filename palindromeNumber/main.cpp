#include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    bool isPalindrome(long long int x) {

        if (x < 0) {
            return false;
        }
        long long int temp = x;
        long long int numberReverse = 0;
        while(temp > 0) {
            numberReverse = (numberReverse * 10) + (temp % 10);
            temp /= 10;

        }
        if (numberReverse == x) {
            return true;
        }
        return false;
    }
};

int main() {
    Solution solution;
    cout << solution.isPalindrome(121) << '\n';

}
