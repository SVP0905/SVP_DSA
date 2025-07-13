class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i,j=0,0
        m,n=len(g),len(s)
        cnt=0
        while i<m and j<n:
            if g[i]<=s[j]:
                cnt+=1
                i+=1
                j+=1
            else:
                j+=1
        return cnt