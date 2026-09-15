class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = budget = nums[0]
        for i in range(1, len(nums)):
            if budget < 0:
                budget = 0
            budget += nums[i]
            best = max(best, budget)
    
        return best