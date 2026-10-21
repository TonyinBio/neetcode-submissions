class Solution {
public:
    int missingNumber(vector<int>& nums) {
        uint32_t n = nums.size();
        uint32_t total = n * (n + 1) / 2;
        for (uint32_t i = 0; i < n; ++i) {
            total -= nums[i];
        }
        return total;
    }
};
