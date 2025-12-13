class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res=[]
        chars='abc'

        def dfs(path):
            if len(path)==n:
                res.append(''.join(path.copy()))
                return
            
            for ch in chars:
                if path and path[-1]==ch:
                    continue
                path.append(ch)
                dfs(path)
                path.pop()
        
        dfs([])
        return '' if len(res)<k else res[k-1]