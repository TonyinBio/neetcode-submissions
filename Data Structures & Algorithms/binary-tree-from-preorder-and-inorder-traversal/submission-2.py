from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        pptr = 0
        root_id = preorder[0]
        root = TreeNode(root_id)
        
        mp = {val: idx for idx, val in enumerate(inorder)}

        stack = []
        node = root
        sen_pos = math.inf
        while pptr < n - 1:
            # print(node.val, preorder[pptr + 1], sen_pos, end=" ")
            val = node.val
            next_val = preorder[pptr + 1]
            if mp[next_val] < mp[val]: # left node
                # print("left")
                new_node = TreeNode(preorder[pptr + 1])
                node.left = new_node
                stack.append((node, sen_pos))
                sen_pos = mp[val]
                node = new_node
                pptr += 1
            elif mp[next_val] < sen_pos: # right node
                # right node
                # print("right")
                new_node = TreeNode(preorder[pptr + 1])
                node.right = new_node
                stack.append((node, sen_pos))
                node = new_node
                pptr += 1
            else: # backtrack
                # we are at a leaf node. backtrack up
                # print("backtrack")
                node, sen_pos = stack.pop()
        return root
