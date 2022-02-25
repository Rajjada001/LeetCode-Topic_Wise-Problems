# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

def removeDuplicates(a):
    k = 0

    for num in a:
        if k < 2 or num > a[k-2]:
            a[k] = num
            k += 1
    return k



# test cases
t = int(input("Test cases:"))
for _ in range(t):
    print("Enter array elements")
    a = list(map(int, input().split()))
    print(removeDuplicates(a))



