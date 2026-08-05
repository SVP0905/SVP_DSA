class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj_list=defaultdict(list)

        for u,v in invocations:
            adj_list[u].append(v)

        visited=set()        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in adj_list[node]:
                dfs(nei)


        dfs(k)

        # nodes_to_be_deleted=set()
        res=[]
        for a,b in invocations:
            if b in visited and a not in visited:
                return list(range(n))
        

        return [m for m in range(n) if m not in visited]
        
        
    



