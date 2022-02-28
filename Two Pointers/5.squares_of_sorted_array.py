# https://leetcode.com/problems/squares-of-a-sorted-array/

def sorted_squares(a):
    # loop through end to start
    k = 0
    l,r = 0,len(a)-1
    res = [0] * len(a)
    for i in range(len(a)-1,-1,-1):
        if abs(a[l]) > abs(a[r]):
            res[i] = a[l] * a[l]
            l += 1
        else:
            res[i] = a[r] * a[r]
            r -= 1

    return res

t = int(input("Test cases:"))
for _ in range(t):
    print("Enter array elements")
    nums = list(map(int, input().split()))
    print(sorted_squares(nums))