class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int n = matrix[0].size(), m = matrix.size();
        vector<vector<int>> indegrees(m, vector<int>(n, 0));
        queue<pair<int, int>> q;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                for (auto dir : directions) {
                    int next_i = i + dir[0];
                    int next_j = j + dir[1];
                    if (next_i < 0 || next_i >= m ||
                        next_j < 0 || next_j >= n ||
                        matrix[next_i][next_j] >= matrix[i][j]) {
                            continue;
                        }
                    indegrees[i][j] += 1;
                }
                if (indegrees[i][j] == 0) {
                    q.push({i, j});
                }
            }
        }

        int layers_processed = 0;
        while (!q.empty()) {
            int layer_size = q.size();
            for (int itr = 0; itr < layer_size; ++itr) {
                auto [i, j] = q.front();
                q.pop();
                for (auto dir : directions) {
                    int next_i = i + dir[0];
                    int next_j = j + dir[1];
                    if (next_i < 0 || next_i >= m ||
                        next_j < 0 || next_j >= n ||
                        matrix[next_i][next_j] <= matrix[i][j]) {
                            continue;
                        }
                    indegrees[next_i][next_j] -= 1;
                    if (indegrees[next_i][next_j] == 0) {
                        q.push({next_i, next_j});
                    }
                }
            }
            ++layers_processed;
        }
        return layers_processed;
    }

private:
    vector<vector<int>> directions = {
        {-1, 0},
        {1, 0}, 
        {0, -1},
        {0, 1}
    };
};
