"""
Problem: Reverse a string without using slicing or reverse()
Approach: Two-pointer technique
Time Complexity: O(n)
Space Complexity: O(n)
"""


levi = "shri vishwakarma skill university is first skill university in india"
def back(a):
    s = list(a)
    left = 0
    right = len(s)-1
    while left<right:
        s[left],s[right] = s[right],s[left] 
        left+=1
        right-=1
    return "".join(s)

print(back(levi))
