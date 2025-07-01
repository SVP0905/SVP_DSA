class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n=len(s)
        v=[]
        for ch in s:
            if ch.isalpha():
                v.append(ch)
        v.reverse()
        res=[]
        i=0
        for ch in s:
            if ch.isalpha():
                res.append(v[i])
                i+=1
            else:
                res.append(ch)
        return ''.join(res,)