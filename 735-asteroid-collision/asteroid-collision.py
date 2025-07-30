class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for new_asteroid in asteroids:
            survived=True
            while stack and new_asteroid<0<stack[-1]:
                if abs(new_asteroid)<abs(stack[-1]):
                    survived=False
                    break
                elif abs(new_asteroid)==abs(stack[-1]):
                    stack.pop()
                    survived=False
                    break
                else:
                    stack.pop()
            if survived:
                stack.append(new_asteroid)
        
        return stack