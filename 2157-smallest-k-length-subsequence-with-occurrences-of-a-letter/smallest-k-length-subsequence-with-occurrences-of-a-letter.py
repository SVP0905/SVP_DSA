class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        n=len(s)
        stack=[]
        letter_cnt_in_s=s.count(letter)
        letter_cnt_in_stack=0

        for i,ch in enumerate(s):
            while stack and ch<stack[-1]:
                #check1: length check
                if len(stack)-1+(n-i)<k:
                    break
                
                #check2: repetition
                if stack[-1]==letter:
                    if letter_cnt_in_stack-1+letter_cnt_in_s<repetition:
                        break
                
                popped=stack.pop()
                if popped==letter:
                    letter_cnt_in_stack-=1
            
        
            if ch==letter:
                if len(stack)<k:
                    stack.append(ch)
                    letter_cnt_in_stack+=1
            else:
                if len(stack)<k and k-len(stack)>(repetition-letter_cnt_in_stack):
                    stack.append(ch)
            
            if ch==letter:
                letter_cnt_in_s-=1
            

        return ''.join(stack)
