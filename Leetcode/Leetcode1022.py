# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node,temp):
            if not node.left and not node.right:
                temp += str(node.val)
                self.res += int(temp,2)
                return
            temp += str(node.val)
            if node.left:
                dfs(node.left,temp)
            if node.right:
                dfs(node.right,temp)
            

        self.res = 0
        dfs(root,'')
        return self.res        
        
