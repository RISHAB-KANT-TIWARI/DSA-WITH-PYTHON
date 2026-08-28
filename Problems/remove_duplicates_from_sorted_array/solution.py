class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        i = 0
        a = 1
        while i<len(nums)-1:
            if nums[i]!=nums[i+1]:
                nums[a]=nums[i+1]
                a+=1
                count+=1
            i+=1
        return count
        
