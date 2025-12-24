class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples=sum(apple)
        capacity.sort(reverse=True)
        res=0
        for i,cap in enumerate(capacity):
            total_apples-=cap
            if total_apples<=0:
                res=i+1
                break

        return res   
        