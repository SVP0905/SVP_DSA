class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=set('aeiouAEIOU')
        v=[]
        for ch in s:
            if ch in vowels:
                v.append(ch)
        v.reverse()
        i=0
        res=[]
        for ch in s:
            if ch not in vowels:
                res.append(ch)
            if ch in vowels:
                res.append(v[i])
                i+=1
        return ''.join(res)