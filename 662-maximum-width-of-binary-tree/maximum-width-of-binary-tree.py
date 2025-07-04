# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width=0
        q=deque([(root,0)])

        while q:
            len_q=len(q)
            last_pos=q[-1][1]
            first_pos=q[0][1]

            path_width=last_pos-first_pos+1
            max_width=max(max_width,path_width)

            for _ in range(len_q):
                node,pos=q.popleft()
                if node.left:
                    q.append((node.left,2*pos))
                if node.right:
                    q.append((node.right,2*pos+1))
        
        return max_width
