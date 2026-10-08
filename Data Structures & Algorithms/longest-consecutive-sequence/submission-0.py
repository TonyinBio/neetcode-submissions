class Node:
    def __init__(self, right, left, length=1):
        self.length = length
        self.right = right
        self.left = left
    def __repr__(self):
        return str(self.length)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        right = {}
        left = {}
        for num in nums:
            node = Node(num + 1, num)
            if num + 1 not in right:
                right[num + 1] = node
            # if num not in left:
                left[num] = node
            
        # merge sequences O(n) (max 2n merges)
        if len(nums) == 0: return 0
        best_len = 1
        # while right:
        for r in right:
            # r = next(iter(right))
            # print(right)
            # print(left)
            # print()
            if r in left:
                # print(r, end=" ")
                # merge(r, left[r])
                new_len = left[r].length + right[r].length
                # print(new_len)
                best_len = max(best_len, new_len)
                node = Node(left[r].right, right[r].left, new_len)
                right[left[r].right] = node
                left[right[r].left] = node
                # left.pop(r)
                # right.pop(r)
        # print(right)
        # print(left)
        return best_len