class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj_graph=defaultdict(list)

        for u,v,dist in roads:
            adj_graph[u].append((v,dist))
            adj_graph[v].append((u,dist))

        visited=set()
        def dfs(u,dist):
            nonlocal res
            visited.add(u)
            
            for nei,nei_dist in adj_graph[u]:
                res=min(res,nei_dist)
                if nei in visited:
                    continue
                dfs(nei,res)
        
        res=float('inf')
        dfs(1,res)
        return res

        return res

                