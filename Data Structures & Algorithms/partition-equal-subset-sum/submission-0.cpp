class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int total = std::accumulate(nums.begin(), nums.end(), 0);
        if (total % 2 == 1) {
            return false;
        }
        int half = total / 2;
        // std::vector<std::vector<int>>> table(nums.size(), std::vector());
        
        return canCreate(half, nums);
    }

private:
    bool canCreate(int target, vector<int>& nums) {
        if (target == 0) {
            return true;
        } else if (target < 0) {
            return false;
        }
        for (int& num : nums) {
            if (num == -1) {
                continue;
            }
            int temp = num;
            int new_target = target - num;
            num = -1;
            if (canCreate(new_target, nums)) {
                return true;
            }
            num = temp;
        }
        return false;
    }
};
