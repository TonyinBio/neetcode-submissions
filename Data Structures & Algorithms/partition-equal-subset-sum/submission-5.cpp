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
    unordered_map<long long, bool> memo;
    long long hash(int x, int y) {
        return (static_cast<long long>(x) << 32) | y;
    }
    bool canCreate(int target, int i, vector<int>& nums) {
        if (target == 0) {
            return true;
        } else if (target < 0) {
            return false;
        } else if (i == nums.size()) {
            return false;
        } 
        auto it = memo.find(hash(target, i));
        if (it != memo.end()) {
            return it->second;
        }
        int newTarget = target - nums[i];
        bool result = canCreate(newTarget, i + 1, nums) || canCreate(target, i + 1, nums);
        memo[hash(target, i)] = result;
        return result;
    }
};
