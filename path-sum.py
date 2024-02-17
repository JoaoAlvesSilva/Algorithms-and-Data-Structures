// https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root == None:
            return False
        
        level = 0
        nodes = [[root]]

        #BFS algorithm
        while True:
            layer = []
            for node in nodes[level]:
                if node.left != None:
                    node.left.val = node.val + node.left.val
                    layer.append(node.left)
                if node.right != None:
                    node.right.val = node.val + node.right.val
                    layer.append(node.right)
                if node.left == None and node.right == None:
                    #found a leaf
                    if node.val == targetSum:
                        return True
            level += 1
            nodes.append(layer)
            if layer == []:
                break
        return False


        