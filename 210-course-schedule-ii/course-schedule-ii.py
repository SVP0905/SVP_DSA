class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        indegree=defaultdict(int)
        for v,u in prerequisites:
            graph[u].append(v)
            indegree[v]+=1
        
        q=deque([x for x in range(numCourses) if indegree[x]==0])

        order=[]
        while q:
            node=q.popleft()
            order.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        
        return order if len(order)==numCourses else []