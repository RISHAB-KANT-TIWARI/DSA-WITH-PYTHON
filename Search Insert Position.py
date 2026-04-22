# Problem: Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/
# Difficulty: Easy

# Summary:
# Given a sorted array, return index of target or position to insert.

# Approach:
# Binary Search

# Time: O(log n)
# Space: O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        last = len(nums)-1
        ans = len(nums)
        while i<=last:
            mid = (i+last)//2
            if target<=nums[mid]:
                ans = mid
                last = mid-1
            else:
                i = mid+1
        return ans
        
