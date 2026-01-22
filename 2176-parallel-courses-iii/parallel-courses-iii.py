class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj_list=defaultdict(list)
        indegree=[0]*n
        for u,v in relations:
            adj_list[u-1].append(v-1)
            indegree[v-1]+=1
        
        q=deque()
        max_time=[0]*n

        for node in range(n):
            if indegree[node]==0:
                q.append(node)
                max_time[node]=time[node]
        

        while q:
            node=q.popleft()
            for nei in adj_list[node]:
                max_time[nei]=max(max_time[nei],max_time[node]+time[nei])
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        
        return max(max_time)
