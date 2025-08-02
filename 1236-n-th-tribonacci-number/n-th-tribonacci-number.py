class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1:
            return 1
            
        prev1,prev2,cur=0,1,1

        for i in range(3,n+1):
            temp=prev1+prev2+cur
            prev1,prev2,cur=prev2,cur,temp
        return cur
        