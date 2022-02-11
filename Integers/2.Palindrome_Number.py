# https://leetcode.com/problems/palindrome-number/

def palindome(n):
    # Approach 1: Two Pointers
    if(n<0):
        return False

    string = str(n)
    left,right = 0,len(string)-1

    while(left < right):
        if(string[left] != string[right]):
            return False
        left+=1
        right-=1

    return True

    '''
    # Approach 2:
    return str(x)==str(x)[::-1]
    '''

t = int(input("Test Cases:"))
for _ in range(t):
    n = int(input("Enter n:"))
    print(palindome(n))


