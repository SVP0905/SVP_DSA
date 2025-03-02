class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n1=len(nums1)
        n2=len(nums2)
        i=0
        j=0
        res=[]
        while i<n1 and j<n2:
            if nums1[i][0]==nums2[j][0]:
                sum_=nums1[i][1]+nums2[j][1]
                res.append([nums1[i][0],sum_])
                i+=1
                j+=1
            elif nums1[i][0]<nums2[j][0]:
                res.append([nums1[i][0],nums1[i][1]])
                i+=1
            else:
                res.append([nums2[j][0],nums2[j][1]])
                j+=1
        
        while i<n1:
            res.append([nums1[i][0],nums1[i][1]])
            i+=1
        while j<n2:
            res.append([nums2[j][0],nums2[j][1]])
            j+=1
        return res