class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        start = 0
        temp = 0
        while start<len(nums):
            if 0<nums[start]<=len(nums):
                if start!=nums[start]-1:
                    temp = nums[start]
                    if nums[temp-1]==temp:
                        start+=1
                    else:
                        nums[start]=nums[temp-1]
                        nums[temp-1]=temp
                        start+=0
                else:
                    start+=1
            else:
                start+=1
        left = 0
        count = 0
        while left<len(nums):
            if left!=nums[left]-1:
                count = left+1
                break
            else:
                left+=1
        if count==0:
            return len(nums)+1
        else:
            return count
        
