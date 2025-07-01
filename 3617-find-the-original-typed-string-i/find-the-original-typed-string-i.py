class Solution:
    def possibleStringCount(self, word: str) -> int:
        res=1
        for i in range(1,len(word)):
            if word[i-1]==word[i]:
                res+=1
        return res
