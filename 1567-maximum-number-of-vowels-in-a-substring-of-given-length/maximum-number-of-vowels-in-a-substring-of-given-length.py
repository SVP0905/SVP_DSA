class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={'a','e','i','o','u'}
        max_=0
        for i in range(k):
            if s[i] in vowels:
                max_+=1
        cur=max_
        for i in range(k,len(s)):
            if s[i] in vowels:
                cur+=1
            if s[i-k] in vowels:
                cur-=1
            max_=max(cur,max_)
        return max_