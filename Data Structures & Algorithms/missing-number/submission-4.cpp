class Solution {
public:
    int missingNumber(vector<int>& nums) {
        size_t result = nums.size();
        for (size_t i = 0; i < nums.size(); ++i) {
            result ^= i ^ nums[i];
        }
        return result;
    }
};
