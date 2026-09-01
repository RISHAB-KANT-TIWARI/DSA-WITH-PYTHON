class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x>=0 and x<10:
            return True
        else:
            reverse=[]
            word=list(str(x))
            for i in range(len(word)-1,-1,-1):
                reverse.append(word[i])
            if word==reverse:
                return True
            else:
                return False
