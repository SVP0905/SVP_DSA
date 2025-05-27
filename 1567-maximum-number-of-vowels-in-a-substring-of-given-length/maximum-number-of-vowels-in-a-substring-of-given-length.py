class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set('aeiou')

        current=sum([1 for i in range(k) if s[i] in vowels])
        res=current

        for i in range(k,len(s)):
            current+=(s[i] in vowels)-(s[i-k] in vowels)
            res=max(res,current)
        
        return res