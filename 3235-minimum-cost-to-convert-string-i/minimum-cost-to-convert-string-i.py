class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj=defaultdict(list)

        for i in range(len(original)):
            adj[ord(original[i])-ord('a')].append((cost[i],ord(changed[i])-ord('a')))
        
        def dijkstra(s):
            dist=[float('inf')]*26
            dist[s]=0
            h=[(0,s)] #wei,node

            while h:
                w,n=heapq.heappop(h)
                for nw,nei in adj[n]:
                    new_wei=w+nw
                    if new_wei<dist[nei]:
                        dist[nei]=new_wei
                        heapq.heappush(h,(new_wei,nei))
            
            return dist
        
        mn_cost=[dijkstra(i) for i in range(26)]

        n=len(source)
        res=0

        for i in range(n):
            s=ord(source[i])-ord('a')
            d=ord(target[i])-ord('a')

            if mn_cost[s][d]==float('inf'):
                return -1
            
            res+=mn_cost[s][d]
        
        return res

