# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        all_nodes=[]
        def bfs(node):
            nonlocal all_nodes
            if not node:
                return
            q=deque([node])
            while q:
                node=q.popleft()
                all_nodes.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        bfs(root)
        
        def dfs(node,sum_):
            if not node:
                return 0
            cnt=0
            sum_+=node.val
            
            if sum_==targetSum:
                cnt+=1
            
            cnt+=dfs(node.left,sum_)
            cnt+=dfs(node.right,sum_)
            return cnt
        
        cnt=0
        for node in all_nodes:
            cnt+=dfs(node,0)
        
        return cnt
        