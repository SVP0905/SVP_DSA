class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for num in asteroids:
            while stack and stack[-1]>0 and num<0:
                if abs(stack[-1])<abs(num):
                    stack.pop()
                    continue
                elif abs(stack[-1])==abs(num):
                    stack.pop()
                    num=0
                    break
                else:
                    num=0
                    break
            
            if num!=0:
                stack.append(num)

        return stack