class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adj_list=defaultdict(list)

        for i in range(len(graph)):
            for node in graph[i]:
                adj_list[i].append(node)
        
        dist=len(graph)-1

        res=[]

        def dfs(node,parent,path):
            path.append(node)

            if node==dist:
                res.append(path.copy())
            
    
            for nei in adj_list[node]:
                dfs(nei,node,path)

            path.pop()
        

        dfs(0,None,[])

        return res
