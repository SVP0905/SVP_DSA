class Solution:
    def findGCD(self,a,b):
        if b==0:
            return a
        return self.findGCD(b,a%b)

    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        n=len(nums)
        freq=Counter(nums)
        m=max(nums)
        exact_pairs=defaultdict(int)
        
        for gcd_value in range(m,0,-1):
            cnt=0
            for multiple in range(gcd_value,m+1,gcd_value):
                    cnt+=freq[multiple]
            
            total_formed_pairs=cnt*(cnt-1)//2

            for multiple in range(2*gcd_value,m+1,gcd_value):
                total_formed_pairs-=exact_pairs[multiple]
            
            exact_pairs[gcd_value]=total_formed_pairs
        

        gcd_list=[]
        prefix_sums=[]
        current_total=0

        for g in range(1,m+1):
            if exact_pairs[g]>0:
                current_total+=exact_pairs[g]
                gcd_list.append(g)
                prefix_sums.append(current_total)
        
        ans=[]
        for q in queries:
            idx=bisect.bisect_right(prefix_sums,q)
            ans.append(gcd_list[idx])
        
        return ans
        
        


        