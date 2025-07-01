class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res=[]
        for i in range(0,len(s),2*k):
            segment=s[i:i+2*k]
            if len(segment)<k:
                rev_part=segment[::-1]
                remaining_part=''
            else:
                rev_part=segment[:k][::-1]
                remaining_part=segment[k:]
            res.append(rev_part+remaining_part)
        return ''.join(res)