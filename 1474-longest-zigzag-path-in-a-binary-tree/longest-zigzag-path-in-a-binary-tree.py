# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node,dir,len_):
            if not node:
                return len_

            if dir==0:
                path=dfs(node.right,1,len_+1)
                new=dfs(node.left,0,0)
            else:
                path=dfs(node.left,0,len_+1)
                new=dfs(node.right,1,0)

            return max(path,new)
        left=dfs(root.left,0,0)
        right=dfs(root.right,1,0)
        return max(left,right)