class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        jumps = 0
        l = r = 0
        while True:
            best_r = r
            while l <= r:
                if nums[l] + l > best_r:
                    best_r = nums[l] + l
                l += 1
            r = best_r
            jumps += 1
            if r >= len(nums) - 1:
                return jumps