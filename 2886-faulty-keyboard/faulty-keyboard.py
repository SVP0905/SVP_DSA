class Solution:
    def finalString(self, s: str) -> str:
        res=[]
        for i in range(len(s)):
            if s[i]!='i':
                res.append(s[i])
            if s[i]=='i':
                res.reverse()
        return ''.join(res)