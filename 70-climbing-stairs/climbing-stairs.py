class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev,cur=1,1

        for i in range(2,n+1):
            temp=prev+cur
            prev,cur=cur,temp
        return cur