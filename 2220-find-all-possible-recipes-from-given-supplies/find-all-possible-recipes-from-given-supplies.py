class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        cnt=len(recipes)
        visited=[False]*cnt
        supplies=set(supplies)
        res=[]
        for _ in range(cnt):
            for i in range(cnt):
                if visited[i]:
                    continue
                flag=True
                for j in range(len(ingredients[i])):
                    if ingredients[i][j] not in supplies:
                        flag=False
                        break
                
                if flag:
                    res.append(recipes[i])
                    visited[i]=True
                    supplies.add(recipes[i])
        
        return res
            
