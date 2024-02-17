// https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return Solution().InorderTraversal(root)[k-1]
        
    def InorderTraversal(self, root: Optional[TreeNode]) -> list:

        vals = []

        if root == None:
            pass
        else:
            vals += Solution().InorderTraversal(root.left)
            vals.append(root.val)
            vals += Solution().InorderTraversal(root.right)
        return vals


        