class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int total = std::accumulate(nums.begin(), nums.end(), 0);
        if (total % 2 == 1) {
            return false;
        }
        int half = total / 2;
        table = vector<vector<int>>(nums.size(), vector<int>(half + 1, -1));

        return canCreate(half, 0, nums);
    }

private:
    vector<vector<int>> table;
    bool canCreate(int target, int i, vector<int>& nums) {
        if (target == 0) {
            return true;
        } else if (target < 0) {
            return false;
        } else if (i == nums.size()) {
            return false;
        } 
        if (table[i][target] != -1) {
            return static_cast<bool>(table[i][target]);
        }
        int newTarget = target - nums[i];
        bool result = canCreate(newTarget, i + 1, nums) || canCreate(target, i + 1, nums);
        table[i][target] = result;
        return result;
    }
};
