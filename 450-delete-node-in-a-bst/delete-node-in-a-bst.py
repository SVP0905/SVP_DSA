# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(node):
            cur=node
            while cur and cur.left:
                cur=cur.left
            return cur
        def dfs(root,key):
            if not root:
                return None
            
            if key<root.val:
                root.left=dfs(root.left,key)
            elif key>root.val:
                root.right=dfs(root.right,key)
            else:
                if not root.right:
                    return root.left
                elif not root.left:
                    return root.right
                else:
                    minNode=findMin(root.right)
                    root.val=minNode.val
                    root.right=dfs(root.right,minNode.val)
            return root
        return dfs(root,key)