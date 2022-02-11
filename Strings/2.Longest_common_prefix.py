# https://leetcode.com/problems/longest-common-prefix

import enum


def longest_common_prefix(s):
    if s=="": return ""

    # get the minimum value in s by the size. 
    shortest = min(s, key=len)
    print(min(s))
    print(shortest)
    for i,val in enumerate(shortest):
        for ch in s:
            if ch[i] != val:
                return shortest[:i]

    return shortest



print(longest_common_prefix(["flower","flow","flight"]))
print(longest_common_prefix(["abcd", "accd", "adcd"]))
print(longest_common_prefix(["leetcode", "lee", "lead"]))
