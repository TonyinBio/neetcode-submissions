class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for subset_len in range(1, len(nums) + 1):
            stack = [0]
            while stack[0] + subset_len - 1 < len(nums):
                # finish the stack
                while len(stack) < subset_len:
                    stack.append(stack[-1] + 1)
                
                result.append([nums[i] for i in stack])
                
                # cut off what you cant use anymore
                # print(stack)
                top = stack.pop()
                roof = len(nums)
                while top + 1 >= roof and stack:
                    top = stack.pop()
                    roof -= 1
                stack.append(top + 1)
        
        return result