# https://leetcode.com/problems/reverse-words-in-a-string-iii

def reverse_words_in_string3(s): 
#         reverse function
        def reverse(a,l,r):
            while l<=r:
                a[l],a[r] = a[r],a[l]
                l += 1 
                r -= 1
            return a
#     step 1: convert the string to array
        s = list(s)
        curr = 0
        for i in range(len(s)):
#             if we found any white space, reverse the array element before that.
            if s[i]==" ":
#         reverse the array
                reverse(s,curr, i-1)
#             make the current element to the element after i
                curr = i+1 
        reverse(s,curr, len(s)-1)
#         join all the elements in the array as a string. 
        return "".join(s)
            
        

print(reverse_words_in_string3("God Ding"))
print(reverse_words_in_string3("Let's take LeetCode contest"))
