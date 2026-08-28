class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        a = 0
        k = 0
        while i<=len(nums)-1:
            if nums[i]!=val:
                nums[a]=nums[i]
                nums[i]=nums[a]
                a+=1
                k+=1
                
                
            i+=1
        return k
        
        
