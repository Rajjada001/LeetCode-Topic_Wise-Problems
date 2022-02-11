# https://leetcode.com/problems/factorial-trailing-zeroes/

def factorial_trailing_zeroes(n):
    res = 0
    while(n>=5):
        n = n//5
        res += n
    
    return res

t = int(input("Test Cases:"))
for _ in range(t):
    n = int(input("Enter n:"))
    print(factorial_trailing_zeroes(n))
