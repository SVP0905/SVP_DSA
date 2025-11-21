class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_indices={char:i for i,char in enumerate(s)}
        prev,end=0,0
        res=[]

        for i in range(len(s)):
            cur_ch_end=last_indices[s[i]]
            if cur_ch_end>end:
                end=cur_ch_end
            if i==end:
                res.append(end-prev+1)
                prev=i+1
        
        return res