# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        res=[]

        q=deque([root])


        while q:
            cur_q_len=len(q)
            temp=[]
            for _ in range(cur_q_len):
                cur_node=q.popleft()
                temp.append(cur_node.val)

                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)

            res.append(temp)
        
        return res[::-1]