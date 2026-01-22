class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n=len(favorite)
        adj_list=defaultdict(list)

        indegree=[0]*n
        for i in range(n):
            indegree[favorite[i]]+=1
        
        q=deque([i for i in range(n) if indegree[i]==0])

        chain_len=[1]*n
        while q:
            node=q.popleft()
            target=favorite[node]

            chain_len[target]=max(chain_len[target],chain_len[node]+1)

            indegree[target]-=1
            if indegree[target]==0:
                q.append(target)
        

        max_cycle_size=0
        mutual_pair=0
        visited=set()
        for i in range(n):
            if indegree[i]>0 and i not in visited:
                cycle_cnt=0
                curr=i
                
                while curr not in visited:
                    visited.add(curr)
                    curr=favorite[curr]
                    cycle_cnt+=1
                
                if cycle_cnt>2:
                    max_cycle_size=max(max_cycle_size,cycle_cnt)
                elif cycle_cnt==2:
                    node1=i
                    node2=favorite[i]
                    mutual_pair+=chain_len[node1]+chain_len[node2]
        
        return max(max_cycle_size,mutual_pair)