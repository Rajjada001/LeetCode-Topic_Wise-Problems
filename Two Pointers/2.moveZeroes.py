# https://leetcode.com/problems/move-zeroes/

def moveZeroes(a):
    k = 0

    for i in range(len(a)):
        if a[i] != 0:
            a[k] = a[i]
            k+=1

    for i in range(k, len(a)):
        a[k] = 0
        k += 1

    return a



# test cases
t = int(input("Test cases:"))
for _ in range(t):
    print("Enter array elements")
    a = list(map(int, input().split()))
    print(moveZeroes(a))