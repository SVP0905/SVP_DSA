# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        if not root:
            return 

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        
        res=[]
        dfs(root)
        map_=set()
        for num in res:
            diff=k-num
            if diff in map_:
                return True
            map_.add(num)
        return False
        