class Solution:
    def maxDifference(self, s: str) -> int:
        counter=Counter(s)
        even=[]
        odd=[]

        for _,value in counter.items():
            if value%2==0:
                even.append(value)
            else:
                odd.append(value)
        
        return max(odd)-min(even)