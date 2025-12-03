class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        profit=[0]*n
        for i in range(len(nums1)):
            diff=nums2[i]-nums1[i]
            profit[i]=diff
        
        cur_sum,max_sum=0,float('-inf')
        for i in range(len(nums1)):
            cur_sum+=profit[i]

            if cur_sum>max_sum:
                max_sum=cur_sum
            
            if cur_sum<0:
                cur_sum=0
        
        if max_sum>0:
            nums1_gain=sum(nums1)+max_sum
        else:
            nums1_gain=sum(nums1)

        profit=[0]*len(nums2)

        for i in range(len(nums2)):
            diff=nums1[i]-nums2[i]
            profit[i]=diff
        
        cur_sum,max_sum=0,float('-inf')
        for i in range(len(nums2)):
            cur_sum+=profit[i]
            if cur_sum>max_sum:
                max_sum=cur_sum
            if cur_sum<0:
                cur_sum=0
        
        if max_sum>0:
            nums2_gain=sum(nums2)+max_sum
        else:
            nums2_gain=sum(nums2)

        return max(nums1_gain,nums2_gain)