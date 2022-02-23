# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(a):
    k = 1

    for i in range(1,len(a)):
        if a[i] != a[i-1]:
            a[k] = a[i]
            k += 1
    return k



# test cases
t = int(input("Test cases:"))
for _ in range(t):
    print("Enter array elements")
    a = list(map(int, input().split()))
    print(removeDuplicates(a))