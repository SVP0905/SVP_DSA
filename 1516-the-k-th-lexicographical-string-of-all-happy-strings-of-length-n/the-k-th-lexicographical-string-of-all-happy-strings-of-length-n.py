class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def dfs(str_):
            if len(str_)==n:
                res.append(str_)
                return
            
            for c in ['a','b','c']:
                if not str_ or str_[-1]!=c:
                    dfs(str_+c)
        res=[]
        dfs('')

        return res[k-1] if k<=len(res) else ''
