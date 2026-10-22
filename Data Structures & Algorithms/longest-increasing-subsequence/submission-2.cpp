#include <algorithm>

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int16_t> buds;
        
        size_t n = nums.size();
        buds.push_back(nums[0]);

        for (size_t i = 1; i < n; ++i) {
            int16_t num = nums[i];
            auto it = std::lower_bound(buds.begin(), buds.end(), num);
            
            if (it == buds.end()) {
                buds.push_back(num);
            } else {
                *it = num;
            }
        }

        return buds.size();
    }
};
