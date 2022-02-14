# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def longest_substring(s):
    res = l = 0

    charSet = set()

    for r in range(len(s)):
        if s[r] in charSet:
            charSet.remove(s[l])
            l += 1

        charSet.add(s[r])

        res = max(res, r-l+1)

    return res

print(longest_substring("abcabcbb")) # o/p:3
print(longest_substring("hifuhwerfhkjdchdfhdjf")) #o/p: 13