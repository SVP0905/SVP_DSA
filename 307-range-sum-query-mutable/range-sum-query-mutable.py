class NumArray:

    def __init__(self, nums: List[int]):
        self.n=len(nums)
        self.nums=nums[:]
        self.tree=[0]*(4*self.n)
        self.buildTree(0,0,self.n-1)
    
    def buildTree(self,i,low,high):
        if low==high:
            self.tree[i]=self.nums[low]
            return
        
        mid=(low+high)//2
        self.buildTree(2*i+1,low,mid)
        self.buildTree(2*i+2,mid+1,high)

        self.tree[i]=self.tree[2*i+1]+self.tree[2*i+2]

    def update(self, index: int, val: int) -> None:
        self.nums[index]=val
        self._update(0,0,self.n-1,index,val)
    
    def _update(self,i,low,high,ind,val):
        if low==high:
            self.tree[i]=val
            return
        
        mid=(low+high)//2
        left_ch=2*i+1
        right_ch=2*i+2

        if ind<=mid:
            self._update(left_ch,low,mid,ind,val)
        else:
            self._update(right_ch,mid+1,high,ind,val)

        self.tree[i]=self.tree[left_ch]+self.tree[right_ch]
    

        

    def sumRange(self, left: int, right: int) -> int:
        return self._sumRange(0,0,self.n-1,left,right)
    
    def _sumRange(self,i,low,high,l,r):
        # no overlap
        # [l,r][low,high] or [low,high][l,r]
        if r<low or high<l:
            return 0
        
        # complete overlap
        # l<=low<=hight<=r

        if l<=low and high<=r:
            return self.tree[i]
        
        # partial overlap
        mid=(low+high)//2
        left_ch=2*i+1
        right_ch=2*i+2

        left_val=self._sumRange(left_ch,low,mid,l,r)
        right_val=self._sumRange(right_ch,mid+1,high,l,r)

        return left_val+right_val

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)