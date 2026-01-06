# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        def dfs(node,p,q):
            if not node:
                return None
            

            # left,right=None,None
            if p.val<node.val and q.val<node.val:
                return dfs(node.left,p,q)
            elif p.val>node.val and q.val>node.val:
                return dfs(node.right,p,q)
            else:
                return node
        
        return dfs(root,p,q)