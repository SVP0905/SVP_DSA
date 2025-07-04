# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        q=deque([root])
        cnt=0
        while q:
            len_q=len(q)
            for _ in range(len_q):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                cnt+=self.dfs(node,0,targetSum)
        
        return cnt

    def dfs(self,node,sum_,targetSum):
            if not node:
                return 0
            cnt=0
            sum_+=node.val

            if sum_==targetSum:
                cnt+=1
            
            cnt+=self.dfs(node.left,sum_,targetSum)
            cnt+=self.dfs(node.right,sum_,targetSum)

            return cnt