class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) / 2
        for n in nums:
            total -= n
        return int(total)