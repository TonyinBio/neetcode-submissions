# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node.left is None:
                longest_path_left = -1
                left_dia = 0
            else:
                left_dia, longest_path_left = dfs(node.left)
            if node.right is None:
                longest_path_right = -1
                right_dia = 0
            else:
                right_dia, longest_path_right = dfs(node.right)

            dia = longest_path_left + longest_path_right + 2
            longest_path = max(longest_path_left, longest_path_right) + 1
            best_dia = max(left_dia, right_dia, dia)      

            return best_dia, longest_path

        return dfs(root)[0]