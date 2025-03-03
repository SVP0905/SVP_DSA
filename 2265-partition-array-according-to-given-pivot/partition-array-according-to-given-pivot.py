class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        les=[]
        equal=[]
        greater=[]
        for num in nums:
            if num<pivot:
                les.append(num)
            elif num==pivot:
                equal.append(num)
            else:
                greater.append(num)
        
        les.extend(equal)
        les.extend(greater)
        return les