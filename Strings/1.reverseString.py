# https://leetcode.com/problems/reverse-string/

def reverseString(s):
    left,right = 0,len(s)-1

    while(left < right):
        # swap s[left] and s[right]
        s[left],s[right] = s[right],s[left]
        left+=1
        right-=1

    return s


print(reverseString(["h","e","l","l","o"]))
print(reverseString(["H","a","n","n","a","h"]))
