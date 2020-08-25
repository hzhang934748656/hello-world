# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = 0
        self.travel(root)
        return self.res
    def travel(self,node):
        if not node:
            return  
        if node.left:
            if not node.left.left and not node.left.right:
                self.res += node.left.val
            self.travel(node.left)
        if node.right:
            self.travel(node.right)

        
        
        
        
