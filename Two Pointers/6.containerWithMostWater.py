# https://leetcode.com/problems/container-with-most-water/

def maxArea(height):
    l,r = 0,len(height)-1

    res = 0
    while l<r:
        area = (r-l) * min(height[l], height[r])
        res = max(res, area)

        if height[l] < height[r]:
            l += 1

        elif height[l] > height[r]:
            r -= 1
        # for = case, you can shift any pointer. Honestly, it doesn't matter.
        else:
            r -= 1

    return res


t = int(input("Test cases:"))
for _ in range(t):
    print("Enter array elements")
    heights = list(map(int, input().split()))
    print(maxArea(heights))