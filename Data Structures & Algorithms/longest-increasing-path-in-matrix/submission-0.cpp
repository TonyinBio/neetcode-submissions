class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        n = matrix[0].size();
        m = matrix.size();
        int maxLength = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                uint64_t node = (static_cast<uint64_t>(i) << 32) | j;
                maxLength = max(dfs(matrix, node), maxLength);
            }
        }

        return maxLength;
    }
private:
    uint32_t n = 0, m = 0;
    std::unordered_map<uint64_t, int> memo;
    std::vector<std::pair<int, int>> directions = {
        {1, 0},
        {-1, 0},
        {0, 1},
        {0, -1}
    };

    int dfs(vector<vector<int>>& matrix, uint64_t node) {
        if (memo[node]) {
            return memo[node];
        }

        int i = node >> 32;
        int j = static_cast<int>(node);
        int length = 0;

        for (auto dir : directions) {
            int next_i = dir.first + i;
            int next_j = dir.second + j;
            if (
                next_i < 0 || next_i >= m 
                || next_j < 0 || next_j >= n
            ) {
                continue;
            }
            if (matrix[next_i][next_j] <= matrix[i][j]) {
                continue;
            }
            uint64_t child = (static_cast<uint64_t>(next_i) << 32) | next_j;

            int childLength = memo.contains(child) ? memo.at(child) : dfs(matrix, child);
            length = max(length, childLength);
        }
        memo[node] = ++length;

        return memo[node];
    }
};
