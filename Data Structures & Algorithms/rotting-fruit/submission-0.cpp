class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        std::queue<pair<int, int>> q1;
        std::queue<pair<int, int>> q2;
        auto childs = &q1;
        auto next_childs = &q2;

        // std::unordered_set<long long> visited;
        int generation = 0;

        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == 2) {
                    q1.push({i, j});
                }
            }
        }

        while (!childs->empty()) {
            // cout << childs.front().first << ' ' << childs.front().second << endl;
            auto& [i, j] = childs->front();
            if (i - 1 >= 0) {
                rot(grid, i - 1, j, next_childs);
            }
            if (i + 1 < grid.size()) {
                rot(grid, i + 1, j, next_childs);
            }
            if (j - 1 >= 0) {
                rot(grid, i, j - 1, next_childs);
            }
            if (j + 1 < grid[0].size()) {
                rot(grid, i, j + 1, next_childs);
            }
            childs->pop();

            if (childs->empty() && !next_childs->empty()) {
                auto temp = childs;
                childs = next_childs; 
                next_childs = temp;
                ++generation;
            }
        }

        return hasFresh(grid) ? -1 : generation;
    }


private:
    // long long makeKey(int a, int b) {
    //     return ((long long)a << 32 | (b & 0xffffffffL));
    // }
    bool hasFresh(vector<vector<int>>& grid) {
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == 1) return true;
            }
        }
        return false;
    }

    void rot(vector<vector<int>>& grid, int i, int j, std::queue<pair<int, int>>* next_childs) {
        if (grid[i][j] != 1) {
            return;
        }
        grid[i][j] = 2;
        next_childs->push({i, j});
    }
};
