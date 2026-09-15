class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        budget = nums[0]
        i = 1
        while i < len(nums):
            # print(budget)
            # if budget < 0 and nums[i] < 0:
            #     continue
            new_budget = budget + nums[i]
            if new_budget <= 0:

                # print("finding")
                # find new start
                while i < len(nums) - 1 and nums[i] < 0:
                    i += 1
                # print(i)
                new_budget = nums[i]
            budget = new_budget
            best = max(best, budget)
            i += 1
        return best