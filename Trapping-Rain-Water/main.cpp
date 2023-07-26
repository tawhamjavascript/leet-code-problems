#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int max_left = height.front();
        int max_right = height.back();
        int result = 0;

        while (left < right) {
            if (height[left] < height[right]) {
                left ++;
                max_left = max(max_left, height[left]);
                result += max_left - height[left];
            }

            else {
                right --;
                max_right = max(max_right, height[right]);
                result += max_right - height[right];
            }
        }
        return result;

    }
};

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
