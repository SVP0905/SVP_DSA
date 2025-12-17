class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def dfs(i,path):
            if i>=len(pattern):
                return ''.join(map(str,path))
            

            for j in range(1,10):
                if j in path:
                    continue
                
                if not path:
                    path.append(j)
                    res=dfs(i,path) 
                    if res: return res
                    path.pop()
                else:
                    if pattern[i]=='I' and j>path[-1]:
                        path.append(j)
                        res=dfs(i+1,path)
                        if res: return res
                        path.pop()
                    elif pattern[i]=='D' and path[-1]>j:
                        path.append(j)
                        res=dfs(i+1,path)
                        if res: return res
                        path.pop()
        
        return dfs(0,[])
