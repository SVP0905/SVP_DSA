class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n=len(colors)
        res=0
        
        for i in range(n):
            left=colors[i%n]
            middle=colors[(i+1)%n]
            right=colors[(i+2)%n]

            if left!=middle and right!=middle:
                res+=1
        
        return res
        