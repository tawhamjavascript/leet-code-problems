#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_set<char>> cols;
        unordered_map<int, unordered_set<char>> rows;
        unordered_map<string, unordered_set<char>> square;
        for(int i = 0; i < 9; i++) {
            for(int j = 0; j < 9; j++) {
                if(board[i][j] == '.') {
                    continue;
                }
                if(cols[j].count(board[i][j]) > 0 ||
                   rows[i].count(board[i][j]) > 0 ||
                   square[to_string(i / 3) + to_string(j / 3)].count(board[i][j]) > 0 ) {
                    return false;
                }
                cols[j].insert(board[i][j]);
                rows[i].insert(board[i][j]);
                square[to_string(i / 3) + to_string(j / 3)].insert(board[i][j]);
            }
        }
        return true;
    }
};


int main() {

}
