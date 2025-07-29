class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r=0,0
        str_=''
        while l<len(word1) and r<len(word2):
            str_+=word1[l]
            str_+=word2[r]
            l+=1
            r+=1
        
        if l<len(word1):
            str_+=word1[l:]
        if r<len(word2):
            str_+=word2[r:]
        
        return str_