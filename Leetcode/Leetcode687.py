# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        def search(node):
            if not node:
                return 0
            l = search(node.left)
            r = search(node.right)
            left  = right = 0
            if node.left and node.left.val == node.val:
                left= l + 1
            if node.right and node.right.val == node.val:
                right = r + 1 
            self.ans = max(self.ans,left+right)
            return max(left,right)
        search(root)
        return self.ans
        
