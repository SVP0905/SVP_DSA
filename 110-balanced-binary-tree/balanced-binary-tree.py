# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getHeight(self,node):
        if not node:
            return 0
        
        left=self.getHeight(node.left)
        right=self.getHeight(node.right)

        return max(left,right)+1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        if not root:
            return True
        

        left_height=self.getHeight(root.left)
        right_height=self.getHeight(root.right)

        gap_ok=abs(left_height-right_height)<=1

        left_ok=self.isBalanced(root.left)
        right_ok=self.isBalanced(root.right)

        return gap_ok and left_ok and right_ok


                