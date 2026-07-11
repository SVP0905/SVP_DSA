class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_graph=defaultdict(list)
        for u,v in edges:
            adj_graph[u].append(v)
            adj_graph[v].append(u)
        
        visited=set()

        def dfs(node,comp):
            visited.add(node)
            comp.append(node)

            for nei in adj_graph[node]:
                if nei not in visited:
                    dfs(nei,comp)
        
        cnt=0
        for i in range(n):
            if i not in visited:
                comp=[]
                dfs(i,comp)
                
                v_count=len(comp)
                total_edges_in_comp=sum(len(adj_graph[v]) for v in comp)//2

                expected_edges=(v_count*(v_count-1))//2

                if expected_edges==total_edges_in_comp:
                    cnt+=1
        
        return cnt