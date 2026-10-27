class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        size_t m = matrix.size();
        size_t n = matrix[0].size();
        vector<int> result;
        size_t i = 0, j = 0;
        size_t horz_max = n - 1;
        size_t vert_max = m - 1;
        size_t horz_min = 0;
        size_t vert_min = 0;
        int mode = 0;
        // std::cout << i << ' ' << j << std::endl;
        while (result.size() < n * m) {
            result.push_back(matrix[j][i]);
            switch (mode) {
                case 0:
                    if (i < horz_max) {
                        ++i;
                        break;
                    }
                    ++vert_min;
                    mode = (mode + 1) % 4;
                    [[fallthrough]];
                case 1:
                    if (j < vert_max) {
                        ++j;
                        break;
                    }
                    --horz_max;
                    mode = (mode + 1) % 4;
                    [[fallthrough]];
                case 2:
                    if (i > horz_min) {
                        --i;
                        break;
                    }
                    --vert_max;
                    mode = (mode + 1) % 4;
                    [[fallthrough]];
                case 3:
                    if (j > vert_min) {
                        --j;
                        break;
                    }
                    ++horz_min;
                    mode = (mode + 1) % 4;
                    ++i;
            }
        }
        return result;
    }
};
