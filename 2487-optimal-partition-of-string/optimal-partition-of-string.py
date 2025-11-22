class Solution:
    def partitionString(self, s: str) -> int:
        seen=set()
        r=0
        res=1 #as each char is 1 partition
        while r<len(s):
            if s[r] in seen:
                res+=1
                seen=set()
            
            seen.add(s[r])
            r+=1
        
        return res