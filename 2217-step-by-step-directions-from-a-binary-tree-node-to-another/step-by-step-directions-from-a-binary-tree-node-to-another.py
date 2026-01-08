# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node,target,path):
            if not node:
                return False

            if node.val==target:
                return True
            
            path.append('L')
            if dfs(node.left,target,path):
                return True
            path.pop()

            path.append('R')
            if dfs(node.right,target,path):
                return True
            path.pop()
            
            return False
        
        start_path=[]
        dest_path=[]

        dfs(root,startValue,start_path)
        dfs(root,destValue,dest_path)

        print(start_path)
        print(dest_path)

        i=0
        while i<len(start_path) and i<len(dest_path) and start_path[i]==dest_path[i]:
            i+=1
        
        res=''

        for j in range(i,len(start_path)):
            res+='U'

        for j in range(i,len(dest_path)):
            res+=dest_path[j]

        return res

