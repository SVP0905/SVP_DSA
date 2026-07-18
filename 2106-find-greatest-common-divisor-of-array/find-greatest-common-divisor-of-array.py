class Solution:
    def GCD(self,a,b):
        if b==0:
            return a
        else:
            return self.GCD(b,a%b)

    def findGCD(self, nums: List[int]) -> int:
        a,b=min(nums),max(nums)
        return self.GCD(a,b)

        