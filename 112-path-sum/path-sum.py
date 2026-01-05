# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node,sum_):
            if not node:
                return False
            
            cur_sum=node.val+sum_
            
            if not node.left and not node.right:
                return cur_sum==targetSum
            
            left=dfs(node.left,cur_sum)
            right=dfs(node.right,cur_sum)

            return left or right
        
        return dfs(root,0)