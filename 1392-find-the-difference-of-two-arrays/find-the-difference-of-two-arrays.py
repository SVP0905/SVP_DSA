class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        counter1=Counter(nums1)
        counter2=Counter(nums2)

        res=[]

        loc_res=[]
        for key in counter1.keys():
            if key not in counter2:
                loc_res.append(key)
        res.append(loc_res)

        loc_res=[]
        for key in counter2.keys():
            if key not in counter1:
                loc_res.append(key)
        
        res.append(loc_res)

        return res