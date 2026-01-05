# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res=0

        def dfs(node,cur_high):
            nonlocal res
            if not node:
                return
            
            if node.val>=cur_high:
                cur_high=node.val
                res+=1
            
            dfs(node.left,cur_high)
            dfs(node.right,cur_high)
        
        dfs(root,float('-inf'))

        return res
            