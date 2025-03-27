class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        map1=defaultdict(int)
        map2=defaultdict(int)

        for num in nums:
            map2[num]+=1
        
        n=len(nums)
        for i in range(n):
            num=nums[i]
            map2[num]-=1
            map1[num]+=1

            if(map1[num]*2>i+1 and map2[num]*2>n-i-1):
                return i

        return -1