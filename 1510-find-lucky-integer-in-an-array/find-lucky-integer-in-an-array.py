class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter=Counter(arr)
        res=[]
        for key,val in counter.items():
            if key==val:
                res.append(key)
        
        return max(res) if res else -1
