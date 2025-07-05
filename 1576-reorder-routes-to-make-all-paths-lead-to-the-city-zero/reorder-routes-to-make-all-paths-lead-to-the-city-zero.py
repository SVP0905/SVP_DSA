class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph=[[] for _ in range(n)]

        for u,v in connections:
            graph[u].append((v,1))
            graph[v].append((u,0))

        visited=[False]*n


        def dfs(city):
            visited[city]=True

            flips=0

            for nei,cost in graph[city]:
                if not visited[nei]:
                    flips+=cost+dfs(nei)
            
            return flips
        
        return dfs(0)