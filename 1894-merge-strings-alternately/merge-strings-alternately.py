class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r=0,0
        m,n=len(word1),len(word2)
        arr=[]
        while l<m and r<n:
            arr.append(word1[l])
            l+=1
            arr.append(word2[r])
            r+=1
        
        if l<m:
            arr.append(word1[l:])
        if r<n:
            arr.append(word2[r:])
        
        return ''.join(arr)
            