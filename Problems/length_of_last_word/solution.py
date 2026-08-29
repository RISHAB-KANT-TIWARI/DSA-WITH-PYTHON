class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        start = 0
        last = len(s)-1
        while start<=last:
            if s[last]!=" ":
                count+=1
                if s[last-1]==" ":
                    break
            last-=1
        return count

            
