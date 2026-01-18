class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        n=len(s)
        global_cnt=Counter(s)
        stack_cnt=defaultdict(int)
        stack=[]

        for i,ch in enumerate(s):
            global_cnt[ch]-=1

            while stack and ch<stack[-1]:
                top=stack[-1]

                available=global_cnt[top]+stack_cnt[top]

                if available>1:
                    stack.pop()
                    stack_cnt[top]-=1
                else:
                    break

            stack.append(ch)
            stack_cnt[ch]+=1
        
        while stack and stack_cnt[stack[-1]]>1:
            top=stack.pop()
            stack_cnt[top]-=1
            
            
        return ''.join(stack)