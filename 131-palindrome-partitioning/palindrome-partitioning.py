class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]

        def dfs(start_idx,path):
            if start_idx==len(s):
                res.append(path.copy())
                return
            
            for j in range(start_idx,len(s)):
                chunk=s[start_idx:j+1]
                if chunk==chunk[::-1]:
                    path.append(chunk)
                    dfs(j+1,path)
                    path.pop()
        
        dfs(0,[])
        return res