class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        arr=[]
        for i in range(0,len(s),k):
            arr.append(list(s[i:i+k]))
        
        for sub in arr:
            while len(sub)<k:
                sub.append(fill)
        
        res=[]
        for sub in arr:
            res.append(''.join(sub))
        
        return res
        
        