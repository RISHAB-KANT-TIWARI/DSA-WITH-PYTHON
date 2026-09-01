class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        star=""
        freq={}
        start=0
        last=len(s)-1
        maxi=0
        while start<=last:
            if s[start] not in star:
                star+=s[start]
                start+=1
            else:
                freq[star]=len(star)
                for j in range(len(star)):
                    if star[j]==s[start]:
                        star=star[j+1:]
                        break
                star+=s[start]
                start+=1
        for i in freq:
            if freq[i]>maxi:
                maxi=freq[i]
        if len(star)>maxi:
            return len(star)
        else:
            return maxi
            
