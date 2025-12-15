class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=defaultdict(list)

        for s,d in tickets:
            graph[s].append(d)
        
        for node in graph:
            graph[node].sort(reverse=True)

        res=[]

        def dfs(node):
            while node in graph and len(graph[node])>0:
                next_node=graph[node].pop()
                dfs(next_node)
            
            res.append(node)
        
        dfs('JFK')

        return res[::-1]

