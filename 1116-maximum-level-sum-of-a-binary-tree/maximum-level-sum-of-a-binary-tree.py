# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=deque([root])
        max_=float('-inf')
        res=0
        level=1
        while q:
            len_q=len(q)
            sum_=0
            for i in range(len_q):
                node=q.popleft()
                sum_+=node.val
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            if sum_>max_:
                res=level
            max_=max(max_,sum_)
            level+=1
        return res
            



