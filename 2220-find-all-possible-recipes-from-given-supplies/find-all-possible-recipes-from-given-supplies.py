class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies=set(supplies)
        recipe_to_idx = {recipe: i for i, recipe in enumerate(recipes)}
        adj={i:[] for i in range(len(recipes))}
        indegree=[0]*len(recipes)
        res=[]

        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                if ingredient not in supplies:
                    if ingredient in recipe_to_idx:
                        j=recipe_to_idx[ingredient]
                        adj[j].append(i)
                        indegree[i]+=1
                    else:
                        indegree[i]=1000
        
        q=deque()
        for i in range(len(recipes)):
            if indegree[i]==0:
                q.append(i)
        
        while q:
            node=q.popleft()
            res.append(recipes[node])
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        
                
        return res
        
        