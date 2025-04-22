class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArray=[]
        i=j=0

        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                mergedArray.append(nums1[i])
                i+=1
            else:
                mergedArray.append(nums2[j])
                j+=1

        while i<len(nums1):
            mergedArray.append(nums1[i])
            i+=1
        while j<len(nums2):
            mergedArray.append(nums2[j])
            j+=1

        total=0
        total_length=len(mergedArray)

        if total_length%2==1:
            return mergedArray[total_length//2]
        else:
            mid1=total_length//2-1
            mid2=total_length//2
            return (mergedArray[mid1]+mergedArray[mid2])/2.0

            
        