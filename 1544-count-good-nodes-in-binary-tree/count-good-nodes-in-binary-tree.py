# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt=0
        def dfs(node,max_):
            nonlocal cnt
            if not node:
                return 
            
            if node.val>=max_:
                cnt+=1
            
            max_=max(max_,node.val)
            dfs(node.left,max_)
            dfs(node.right,max_)
        
        dfs(root,root.val)
        return cnt