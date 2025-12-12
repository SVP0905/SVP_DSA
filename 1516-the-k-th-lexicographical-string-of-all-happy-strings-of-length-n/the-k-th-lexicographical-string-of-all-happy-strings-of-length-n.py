class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res=[]
        chars='abc'

        def dfs(path):
            if len(path)>=n:
                res.append(''.join(path.copy()))
                return
            

            for i in range(len(chars)):
                if path and chars[i]==path[-1]:
                    continue
                path.append(chars[i])
                dfs(path)
                path.pop()
        

        dfs([])
        
        return '' if len(res)<k else res[k-1]
