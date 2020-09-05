# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorderTravel(node,List):
            if not node:
                return
            if node.left:
                inorderTravel(node.left,List)
            List.append(node.val)
            if node.right:
                inorderTravel(node.right,List)
        res = []
        list_1 = []
        list_2 = []
        inorderTravel(root1,list_1)
        inorderTravel(root2,list_2)
        p1 = p2 = 0
        while p1 < len(list_1) and p2 < len(list_2):
            if list_1[p1] < list_2[p2]:
                res.append(list_1[p1])
                p1 += 1
            else:
                res.append(list_2[p2])
                p2 += 1
        while p1 < len(list_1):
            res.append(list_1[p1])
            p1 += 1
        while p2 < len(list_2):
            res.append(list_2[p2])
            p2 += 1
        return res
            
        
        
        
            
