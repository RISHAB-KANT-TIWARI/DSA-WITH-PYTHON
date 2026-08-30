class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            digits.append(1)
        else:
            last = len(digits)-1
            while last>=0:
                if digits[last]!=9:
                    digits[last]+=1
                    break
                elif digits[last]==9 and last==0:
                    digits.append(0)
                    digits[last]=1
                elif digits[last]==9 and last>0:
                    digits[last]=0            
                last-=1
        return digits
