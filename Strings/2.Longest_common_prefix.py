# https://leetcode.com/problems/longest-common-prefix

import enum


def longest_common_prefix(s):
    if s=="": return ""

    # get the minimum value in s by the size. 
    # Approach 1:
    '''
    shortest = min(s, key=len)
    print(min(s))
    print(shortest)
    for i,val in enumerate(shortest):
        for ch in s:
            if ch[i] != val:
                return shortest[:i]

    return shortest
    '''

    # Approach 2:
    # We just need to compare only maximum and minimum length elements. 
    # If there are any common points, keep iterating.
    # Once the elements mismatched, we will return the array till the mis matched element.
    if not s: return ""
    s1,s2 = min(s),max(s)
    # print(s1,s2)
    i = 0
    while(i<len(s1)):
        if s1[i] != s2[i]:
            return s1[:i]
        i+=1
    
    return s1


print(longest_common_prefix(["flower","flow","flight"]))
print(longest_common_prefix(["abcd", "accd", "adcd"]))
print(longest_common_prefix(["leetcode", "lee", "lead"]))
print(longest_common_prefix(["dog","racecar","car"]))
