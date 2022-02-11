# https://leetcode.com/problems/reverse-words-in-a-string/

def reverse_words_in_string(s):
    # approach 1
    a = list(s.split())
    l,r = 0,len(a)-1
    while l<=r:
        a[l],a[r] = a[r],a[l]
        l += 1
        r -= 1
    
    s = ""
    print(a)
    for i in range(len(a)-1):
        s+= a[i] + " "

    s += a[len(a)-1]
    return s

print(reverse_words_in_string("the sky is blue"))
print(reverse_words_in_string("  hello world  "))