# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class AVLNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.height=1
    
class AVL:
    def __init__(self):
        self.root=None
    

    def get_height(self,node):
        if not node:
            return 0
        else:
            return node.height
        
    
    def get_balance(self,node):
        if not node:
            return 0
        
        return self.get_height(node.left)-self.get_height(node.right)
    
    def update_height(self,node):
        if not node:
            return 0
        
        node.height=1+max(self.get_height(node.left),self.get_height(node.right))
    

    def rotate_right(self,y):
        x=y.left
        t2=x.right

        x.right=y
        y.left=t2

        self.update_height(y)
        self.update_height(x)

        return x
    

    def rotate_left(self,y):
        x=y.right
        t2=x.left

        x.left=y
        y.right=t2

        self.update_height(y)
        self.update_height(x)

        return x
    
    def insert(self,key):
        self.root=self._insert(self.root,key)
    

    def _insert(self,node,key):
        if not node:
            return AVLNode(key)
        
        if key<node.key:
            node.left=self._insert(node.left,key)
        elif key>node.key:
            node.right=self._insert(node.right,key)
        else:
            return node  #duplicates not allowed
        
        self.update_height(node)

        balance=self.get_balance(node)

        if balance>1 and key<node.left.key:
            return self.rotate_right(node)
        
        if balance<-1 and key>node.right.key:
            return self.rotate_left(node)
        

        if balance>1 and key>node.left.key:
            node.left=self.rotate_left(node.left)
            return self.rotate_right(node)
        
        if balance<-1 and key<node.right.key:
            node.right=self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
    


class Solution:
    def inorder(self,root,arr):
        if not root:
            return
        
        self.inorder(root.left,arr)
        arr.append(root.val)
        self.inorder(root.right,arr)
    

    def convert_AVL_to_BST(self,avl_node):
        if not avl_node:
            return None
        
        tree_node=TreeNode(avl_node.key)
        tree_node.left=self.convert_AVL_to_BST(avl_node.left)
        tree_node.right=self.convert_AVL_to_BST(avl_node.right)

        return tree_node
        
        
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr=[]
        self.inorder(root,arr)

        
        avl=AVL()

        for key in arr:
            avl.insert(key)
        
        
        return self.convert_AVL_to_BST(avl.root)
