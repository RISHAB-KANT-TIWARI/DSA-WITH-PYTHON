class Solution:
    def maxArea(self, height: List[int]) -> int:
        start=0
        last=len(height)-1
        volume=0
        max_volume=0
        while start<last:
            if height[start]>height[last]:
                volume=(last-start)*height[last]
                last-=1
            elif height[last]>=height[start]:
                volume=(last-start)*height[start]
                start+=1
            if volume>max_volume:
                max_volume=volume

        return max_volume

        
