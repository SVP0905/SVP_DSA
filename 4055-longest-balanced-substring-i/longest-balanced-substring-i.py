class Solution:
    def longestBalanced(self, s: str) -> int:
        n=len(s)
        max_=0
        for i in range(n):
            map_={}
            for j in range(i,n):
                map_[s[j]]=map_.get(s[j],0)+1
                isEq=len(set(map_.values()))<=1
                if isEq:
                    max_=max(max_,j-i+1)
        
        return max_