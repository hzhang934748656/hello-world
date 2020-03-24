# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                ans.append(curr.val)
                curr = curr.right   
            curr = stack.pop()
            curr = curr.left
        ans.reverse()
        return ans
            
        
        
  #倒叙输出 postorder = reverse(root,right,left)
