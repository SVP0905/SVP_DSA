# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        res=[]

        def dfs(node,path):
            if not node:
                return
            
            path.append(node.val)
            cur_sum=sum(path)

            if not node.left and not node.right:
                if cur_sum==targetSum:
                    res.append(path.copy())
            else:
                dfs(node.left,path)
                dfs(node.right,path)
            
            path.pop()
        
        dfs(root,[])

        return res