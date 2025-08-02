class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def fib(x):
            if x==0:
                return 0
            if x==1:
                return 1
            return fib(x-1)+fib(x-2)
        return fib(n)