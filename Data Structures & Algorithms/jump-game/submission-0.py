class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reached = set()
        if len(nums) > 0: reached.add(0)
        # for i in range(len(nums) - 1, -1, -1):
        for i in range(len(nums)):
            if i in reached:
                for j in range(0, nums[i] + 1):
                    # print(i + j)
                    reached.add(i + j)
        return len(nums) - 1 in reached