# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        map_=defaultdict(list)

        def dfs(node,row,col):
            if not node:
                return
            
            map_[col].append((row,node.val))

            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)

        dfs(root,0,0)

        sorted_res=sorted(map_.items())
        
        res=[]
        for key,nodes in sorted_res:
            sorted_nodes=sorted(nodes)
            vals=[val for row,val in sorted_nodes]
            res.append(vals)
        
        return res
            
