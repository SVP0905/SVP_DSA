class Solution:
    def finalString(self, s: str) -> str:
        l,r=0,0
        n=len(s)
        res=[]
        for i in range(n):
            if s[i]!='i':
                res.append(s[i])
            if s[i]=='i':
                res.reverse()
        
        return ''.join(res)