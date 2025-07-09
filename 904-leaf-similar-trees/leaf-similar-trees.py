# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root,arr):
            if not root:
                return
            if not root.right and not root.left:
                arr.append(root.val)
            dfs(root.left,arr)
            dfs(root.right,arr)
        
        l1,l2=[],[]
        dfs(root1,l1)
        dfs(root2,l2)

        return l1==l2