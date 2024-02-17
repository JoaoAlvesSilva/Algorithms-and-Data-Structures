// https://leetcode.com/problems/delete-node-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root == None:
            return None

        if root.val > key:
            root.left = Solution().deleteNode(root.left, key)
        elif root.val < key:
            root.right = Solution().deleteNode(root.right, key)
        elif root.val == key:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                mi = Solution().MinNode(root.right)
                root.val = mi.val
                root.right = Solution().deleteNode(root.right, mi.val)
        return root

    def MinNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root== None:
            return None
        
        curr = root
        prev =  None
        while curr != None:
            prev = curr
            curr = curr.left
        return prev


        