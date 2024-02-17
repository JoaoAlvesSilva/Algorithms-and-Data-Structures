// https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        vals = []  

        if root == None:
            pass
        else:
            vals += Solution().inorderTraversal(root.left)
            vals.append(root.val)
            vals += Solution().inorderTraversal(root.right)

        return vals


        