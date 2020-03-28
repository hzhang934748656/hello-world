# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.dfs(root,0)
        for i in range(len(self.res)):
            if i % 2 != 0:
                self.res[i].reverse()
        return self.res
    def dfs(self,node,level):
        if not node:
            return

        if len(self.res) == level:
            self.res.append([])
        self.res[level] += [node.val]    
        self.dfs(node.left,level+1)
        self.dfs(node.right,level+1)
        
