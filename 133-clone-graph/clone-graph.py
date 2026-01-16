"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        

        old_to_new={}

        def dfs(cur_node):
            if cur_node in old_to_new:
                return old_to_new[cur_node]
            
            copy=Node(cur_node.val)
            old_to_new[cur_node]=copy
            for nei in cur_node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(node)
