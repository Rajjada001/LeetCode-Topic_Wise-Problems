# https://leetcode.com/problems/3sum-closest/

# Approach: Two pointers
def threeSumClosest(nums, target):
    # sort the array
    nums.sort()
    closestSum = 9999999999
    for i in range(len(nums)-2):
        l,r = i+1,len(nums)-1
        while(l<r):
            currSum = nums[i] + nums[l] + nums[r]
            
            if currSum == target:
                return currSum
            if abs(target-currSum) < abs(target - closestSum):
                closestSum = currSum

            elif currSum < target:
                l += 1

            else:
                r -= 1

    return closestSum

# test cases
t = int(input("Test cases:"))
for _ in range(t):
    print("Enter array elements")
    a = list(map(int, input().split()))
    target = int(input("Enter target:"))
    print(threeSumClosest(a, target))