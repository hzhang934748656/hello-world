# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return
        if self.findSame(s,t):
            return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        
        
    def findSame(self,r1,r2):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        if r1.val != r2.val:
            return False
        return self.findSame(r1.left,r2.left) and self.findSame(r1.right,r2.right)
            
            
        
