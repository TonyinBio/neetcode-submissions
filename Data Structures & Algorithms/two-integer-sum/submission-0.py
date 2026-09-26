class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i, num in enumerate(nums):
            # print(num, diff)
            if diff.get(num) is not None:
                return [diff[num], i]
            diff[target - num] = i