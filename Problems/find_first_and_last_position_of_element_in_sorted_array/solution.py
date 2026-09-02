class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        interval_1 = -1
        interval_2 = -1
        if len(nums)==1:
            if nums[0]==target:
                interval_1=0
                interval_2=0
            return [interval_1,interval_2]
        else:
            left = 0
            right = len(nums)-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid]==target:
                    interval_1=mid
                    right=mid-1
                elif target>nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
            left_2 = 0
            right_2 = len(nums)-1
            while left_2<=right_2:
                mid_1 = (left_2+right_2)//2
                if nums[mid_1]==target:
                    interval_2=mid_1
                    left_2 = mid_1+1
                elif target>nums[mid_1]:
                    left_2 = mid_1+1
                else:
                    right_2 = mid_1-1
            if interval_1==-1 and interval_2!=-1:
                interval_1=interval_2
                return [interval_1,interval_2]
            elif interval_2==-1 and interval_1!=-1:
                interval_2=interval_1
                return [interval_1,interval_2]
            else:
                return [interval_1,interval_2]
        
            
