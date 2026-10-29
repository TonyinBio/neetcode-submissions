class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int total = std::accumulate(nums.begin(), nums.end(), 0);
        if (total % 2 == 1) {
            return false;
        }
        int half = total / 2;
        // std::vector<std::vector<int>>> table(nums.size(), std::vector());
        
        return canCreate(half, 0, nums);
    }

private:
    bool canCreate(int target, int i, vector<int>& nums) {
        if (target == 0) {
            return true;
        } else if (target < 0) {
            return false;
        } else if (i == nums.size()) {
            return false;
        }
        int newTarget = target - nums[i];
        return canCreate(newTarget, i + 1, nums) || canCreate(target, i + 1, nums);
    }
};
