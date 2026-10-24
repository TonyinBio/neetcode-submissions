class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        size_t n = nums.size();
        vector<int> leftMax(n);
        vector<int> rightMax(n);
        rightMax.back() = nums.back();
        leftMax.front() = nums.front();

        for (size_t i = 1; i < n; ++i) {
            if (i % k == 0) {
                leftMax[i] = nums[i];
            } else {
                leftMax[i] = max(leftMax[i - 1], nums[i]);
            }

            if ((n - 1 - i) % k == (k - 1)) {
                rightMax[n - 1 - i] = nums[n - 1 - i];
            } else {
                rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - 1 - i]);
            }
        }

        // for (int x : rightMax) {
        //     cout << x << " ";
        // }
        // cout << endl;
        vector<int> maxes(n - k + 1);
        for (size_t l = 0; l < n - k + 1; ++l) {
            maxes[l] = max(rightMax[l], leftMax[l + k - 1]);
            // std::cout << max(rightMax[l], leftMax[l + k]) << std::endl;
        }

        return maxes;
    }
};
