class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map_=defaultdict(int)
        for i in range(len(s)):
            map_[s[i]]=i
        # print(map_)
        start=0
        end=0
        ans=[]
        for i in range(len(s)):
            end=max(end,map_[s[i]])
            if i==end:
                ans.append(end-start+1)
                start=i+1
        return ans
        