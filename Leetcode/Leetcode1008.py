# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        print(root)
        def travel_tree(node,item):
            if item.val > node.val:
                if node.right:
                    travel_tree(node.right,item)
                else:
                    node.right = item
                    return
            else:
                if node.left:
                    travel_tree(node.left,item)
                else:
                    node.left = item
                    return
        for i in range(1,len(preorder)):
            temp = TreeNode(preorder[i])
            travel_tree(root,temp)

        return root
            
        
        
