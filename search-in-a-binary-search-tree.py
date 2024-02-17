// https://leetcode.com/problems/search-in-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None
        elif root.val == val:
            return root
        elif root.val > val:
            return Solution().searchBST(root.left, val)
        elif root.val < val:
            return Solution().searchBST(root.right, val)
        else:
            print('something unexpected')
            return []
        

        