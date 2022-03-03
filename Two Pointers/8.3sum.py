# https://leetcode.com/problems/3sum/

def three_sum(nums):
        #  base case
    if len(nums) < 2:
        return []
    # sort the array
    nums.sort()
#         declare result list
    res = []
    for i in range(len(nums)-2):
        # check duplicates
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left,right = i+1, len(nums)-1
        
        while left < right:
            currSum = nums[i] + nums[left] + nums[right]
            
            if currSum == 0:
                res.append([nums[i],nums[left],nums[right]])
                # print(res)
                left += 1
                right -= 1
                
                while(left < right and nums[left] == nums[left - 1]):
                    left += 1
                
                while( left < right and nums[right] == nums[right + 1]):
                    right -= 1
            
            elif currSum < 0:
                left += 1
            
            else:
                right -= 1
                
    return res


# test cases
t = int(input("Test cases:"))
for _ in range(t):
    print("Enter array elements")
    a = list(map(int, input().split()))
    print(three_sum(a))