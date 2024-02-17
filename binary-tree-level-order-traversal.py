// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root == None:
            return []

        vals = [[root.val]]
        nodes = [[root]]
        level = 0

        while True:
            layer = []
            for node in nodes[level]:
                if node.left != None:
                    layer.append(node.left)
                if node.right != None:
                    layer.append(node.right)
            if layer != []:
                nodes.append(layer)
                vals.append([node.val for node in layer])
                level += 1
            else:
                break
        return vals


        