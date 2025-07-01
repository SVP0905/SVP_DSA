class Solution:
    def possibleStringCount(self, word: str) -> int:
        res=1
        i=0
        while i<len(word):
            j=i
            while j<len(word) and word[i]==word[j]:
                j+=1
            res+=j-i-1
            i=j
        return res