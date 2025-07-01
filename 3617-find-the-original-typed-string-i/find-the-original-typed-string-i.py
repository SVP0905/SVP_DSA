class Solution:
    def possibleStringCount(self, word: str) -> int:
        res=1
        i,n=0,len(word)
        while i<n:
            j=i
            while j<n and word[i]==word[j]:
                j+=1
            res+=j-i-1
            i=j
        return res