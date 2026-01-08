# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents={}

        def find_parents(node,parent):
            if not node:
                return
            
            parents[node]=parent
            find_parents(node.left,node)
            find_parents(node.right,node)
        
        find_parents(root,None)


        q=deque([target])
        visited=set([target])

        cur_dist=0

        while q:
            if cur_dist==k:
                return [node.val for node in q]
            
            for _ in range(len(q)):
                cur_node=q.popleft()
                for nei in (cur_node.left,cur_node.right,parents[cur_node]):
                    if nei and nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            cur_dist+=1
        
        return []