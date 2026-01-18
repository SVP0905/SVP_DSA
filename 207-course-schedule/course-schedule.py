class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list=defaultdict(list)
        indegree=[0]*numCourses
        for u,v in prerequisites:
            adj_list[u].append(v)
            indegree[v]+=1
        

        q=deque()
        n=0
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
                n+=1
        
        while q:
            node=q.popleft()
            for nei in adj_list[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
                    n+=1
        
        return False if n!=numCourses else True
                
        
