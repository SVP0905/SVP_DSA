# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res=[]
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        min_diff=float('inf')
        for i in range(len(res)-1):
            min_diff=min(min_diff,abs(res[i]-res[i+1]))
        
        return min_diff