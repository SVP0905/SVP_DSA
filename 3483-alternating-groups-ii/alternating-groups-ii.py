class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n=len(colors)
        res=0
        alternating=1
        last_color=colors[0]

        for i in range(1,n+k-1):
            if colors[i%n]==last_color:
                alternating=1
                last_color=colors[i%n]
                continue
            
            alternating+=1

            if alternating>=k:
                res+=1
            
            last_color=colors[i%n]

        return res