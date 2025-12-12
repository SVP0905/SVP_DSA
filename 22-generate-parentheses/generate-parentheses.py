class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        map_={'(':n,')':n}

        def dfs(path):
            if len(path)==2*n:
                res.append(''.join(path))
                return

            if map_['(']>0:
                path.append('(')
                map_['(']-=1
                dfs(path)
                path.pop()
                map_['(']+=1

            if map_[')']>map_['(']:
                path.append(')')
                map_[')']-=1
                dfs(path)
                path.pop()
                map_[')']+=1

        dfs([])
        return res    
