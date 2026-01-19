class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph=defaultdict(list)
        indegree=defaultdict(int)
        available=set(supplies)

        for i,r in enumerate(recipes):
            for ing in ingredients[i]:
                if ing not in available:
                    graph[ing].append(r)
                    indegree[r]+=1
        
        q=deque([r for r in recipes if indegree[r]==0])
        res=[]
        while q:
            node=q.popleft()
            res.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        
        return res