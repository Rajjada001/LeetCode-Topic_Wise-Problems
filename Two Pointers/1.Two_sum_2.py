# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

def twoSum_II(nums, target):
    nums.sort()
    l,r = 0, len(nums)-1
    while l <=r:
        currSum = nums[l] + nums[r]

        if currSum == target:
            return [l+1,r+1]
        
        elif currSum < target:
            l += 1
        else:
            r -= 1
    return -1


# test cases
t = int(input("Test cases:"))
for _ in range(t):
    print("Enter array elements")
    a = list(map(int, input().split()))
    target = int(input("Enter target:"))
    print(twoSum_II(a, target))