class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def get_topological_order(graph,indegree):
            q=deque([i for i in range(len(graph)) if indegree[i]==0])
            topo_order=[]
            while q:
                node=q.popleft()
                topo_order.append(node)
                for nei in graph[node]:
                    indegree[nei]-=1
                    if indegree[nei]==0:
                        q.append(nei)
            return topo_order if len(topo_order)==len(graph) else []

        for u in range(len(group)):
            if group[u]==-1:
                group[u]=m
                m+=1

        items_graph={i:[] for i in range(n)}
        items_indegree=[0]*n

        groups_graph={i:[] for i in range(m)}
        groups_indegree=[0]*m

        for u in range(n):
            for v in beforeItems[u]:
                items_graph[v].append(u)
                items_indegree[u]+=1
                if group[u]!=group[v]:
                    groups_graph[group[v]].append(group[u])
                    groups_indegree[group[u]]+=1
        
        items_order=get_topological_order(items_graph,items_indegree)
        groups_order=get_topological_order(groups_graph,groups_indegree)

        if not items_order or not groups_order:
            return []
        
        order_within_group={i:[] for i in range(len(groups_order))}

        for v in items_order:
            order_within_group[group[v]].append(v)
        
        res=[]
        for group in groups_order:
            res+=order_within_group[group]
        
        return res

        

    
        