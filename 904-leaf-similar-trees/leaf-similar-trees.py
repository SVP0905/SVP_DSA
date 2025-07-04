# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node,arr):
            if not node:
                return
            if not node.left and not node.right:
                arr.append(node)
            
            dfs(node.left,arr)
            dfs(node.right,arr)
        l1,l2=[],[]
        dfs(root1,l1)
        dfs(root2,l2)

        if len(l1)!=len(l2):
            return False
        
        for i in range(len(l1)):
            if l1[i].val!=l2[i].val:
                return False
        return True
        
        