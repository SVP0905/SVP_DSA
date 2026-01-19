class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        new_graph=defaultdict(list)
        for i in range(n):
            for v in graph[i]:
                new_graph[v].append(i)
        
        indegree=[0]*n
        for i in range(n):
            for v in new_graph[i]:
                indegree[v]+=1
        
        q=deque([i for i in range(n) if indegree[i]==0])

        res=[i for i in range(n) if indegree[i]==0]
        while q:
            node=q.popleft()
            for nei in new_graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
                    res.append(nei)
        
        return sorted(res)
