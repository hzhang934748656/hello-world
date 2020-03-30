# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -float('inf')
        self.search(root)
        return self.ans
    def search(self,node):
        if not node:
            return 0
        left_sum = max(self.search(node.left),0)
        right_sum = max(self.search(node.right),0)
        all_sum = node.val + left_sum + right_sum
        self.ans = max(self.ans,all_sum)
        return max(node.val + left_sum,node.val + right_sum)
            
        
