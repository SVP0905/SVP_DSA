# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,arr):
        if not root:
            return 
        
        self.inorder(root.left,arr)
        arr.append(root.val)
        self.inorder(root.right,arr)
        

        

    def build_balanced_BST(self,arr,l,r):
        if l>r:
            return None
            
        mid=(l+r)//2
        node=TreeNode(arr[mid])

        node.left=self.build_balanced_BST(arr,l,mid-1)
        node.right=self.build_balanced_BST(arr,mid+1,r)

        return node

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        arr=[]
        self.inorder(root,arr)

        return self.build_balanced_BST(arr,0,len(arr)-1)

        