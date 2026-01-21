class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
            
        degree=[0]*n
        adj_list=defaultdict(list)
        for u,v in edges:
            degree[v]+=1
            degree[u]+=1
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        
        
        q=deque([i for i in range(n) if degree[i]==1])


        remaining_nodes=n
        while remaining_nodes>2:
            leaves=len(q)
            remaining_nodes-=leaves

            for _ in range(len(q)):
                leaf=q.popleft()
                for nei in adj_list[leaf]:
                    degree[nei]-=1
                    if degree[nei]==1:
                        q.append(nei)
        
        return list(q)