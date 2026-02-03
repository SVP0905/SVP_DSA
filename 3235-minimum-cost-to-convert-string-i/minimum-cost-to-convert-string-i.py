class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj_list=defaultdict(list)

        for u,v,wei in zip(original,changed,cost):
            adj_list[u].append((wei,v))

        global_map=defaultdict(dict)

        @cache
        def dijkstra(s):
            map_=defaultdict(lambda : float('inf'))

            map_[s]=0

            h=[(0,s)]

            while h:
                wei,node=heapq.heappop(h)

                for nei_wei,nei in adj_list[node]:
                    if nei_wei+wei<map_[nei]:
                        map_[nei]=nei_wei+wei
                        heapq.heappush(h,(nei_wei+wei,nei))

            return map_


        for s in source:
            global_map[s]=dijkstra(s)
        

        n=len(source)
        res=0
        for i in range(n):
            if source[i]==target[i]:
                continue
            elif source[i]!=target[i]:
                cost=global_map[source[i]].get(target[i],float('inf'))
                if cost==float('inf'):
                    return -1
                else:
                    res+=cost
        
        return res

