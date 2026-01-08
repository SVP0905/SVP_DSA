# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        pre=[]

        def dfs(node):
            if not node:
                pre.append('N')
                return
            
            pre.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(pre)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.i=0
        vals=data.split(',')

        def dfs():
            if self.i>=len(data):
                return 
            
            val=vals[self.i]
            self.i+=1

            if val=='N':
                return None

            node=TreeNode(int(val))

            node.left=dfs()
            node.right=dfs()

            return node
        
        return dfs()


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))