class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        include = [0] * n
        include[0] = 1
        exclude = [0] * n
        for i in range(1, n):
            num = nums[i]
            exclude[i] = max(include[i - 1], exclude[i - 1])
            for j in range(i - 1, -1, -1):
                if nums[j] < num:
                    include[i] = max(include[i], include[j])
            include[i] += 1

        # print(include)
        # print(exclude)
        return max(include[-1], exclude[-1])
