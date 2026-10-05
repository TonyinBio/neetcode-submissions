class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        prefix[0] = nums[0]
        suffix[n - 1] = nums[n - 1]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
        for i in range(n - 2, 0, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        
        result = [1] * n
        result[0] = suffix[1]
        result[n - 1] = prefix[n - 2]
        for i in range(1, n - 1):
            result[i] = prefix[i - 1] * suffix[i + 1]
        return result