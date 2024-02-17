// https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root == None:
            return []
        
        nodes = [[root]]
        level = 0

        while True:
            layer = []
            for node in nodes[level]:
                if node.left != None:
                    layer.append(node.left)
                if node.right != None:
                    layer.append(node.right)
            
            if layer == []:
                break
            else:
                nodes.append(layer)
                level += 1
        return [layer[-1].val for layer in nodes]


        